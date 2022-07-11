#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include<time.h>
void calcul()
{
    unsigned char output[EVP_MAX_MD_SIZE];   //保存输出数组
    unsigned int len, i;
    EVP_MD_CTX* ctx;                         //消息摘要
    ctx = EVP_MD_CTX_new();//调用函数初始化
    char msg1[] = "20220705";              //待计算的消息
    EVP_MD_CTX_init(ctx);                    //初始化摘要结构体
    EVP_DigestInit_ex(ctx, EVP_sm3(), NULL); //设置摘要算法和密码算法引擎，这里密码算法使用sm3，算法引擎使用OpenSSL默认引擎即软算法
    EVP_DigestUpdate(ctx, msg1, strlen(msg1));//调用摘要UpDate计算msg1的摘要
    EVP_DigestFinal_ex(ctx, output, &len);//摘要结束，输出摘要值   
    EVP_MD_CTX_reset(ctx);                       //释放内存

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
