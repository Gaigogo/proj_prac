#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include<time.h>
void calcul()
{
    unsigned char output[EVP_MAX_MD_SIZE];   //保存输出数组
    unsigned int len, i;
    EVP_MD_CTX* ctx;                         
    ctx = EVP_MD_CTX_new();
    char msg1[] = "20220705";              
    EVP_MD_CTX_init(ctx);                    
    EVP_DigestInit_ex(ctx, EVP_sm3(), NULL); 
    EVP_DigestUpdate(ctx, msg1, strlen(msg1));
    EVP_DigestFinal_ex(ctx, output, &len);  
    EVP_MD_CTX_reset(ctx);                       

    printf("%s的hash:\n", msg1);
    for (i = 0; i < len; i++)
    {
        printf("0x%x ", output[i]);
    }
    printf("\n");
}
int main()
{
    OpenSSL_add_all_algorithms();
    clock_t begin, end;
    begin = clock();
    calcul();
    end = clock();
    printf("%fseconds\n", (end - begin) / CLOCKS_PER_SEC);
    return 0;
}
