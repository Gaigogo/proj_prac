#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include<time.h>
void calcul()
{
    unsigned char output[EVP_MAX_MD_SIZE];   //�����������
    unsigned int len, i;
    EVP_MD_CTX* ctx;                         //��ϢժҪ
    ctx = EVP_MD_CTX_new();//���ú�����ʼ��
    char msg1[] = "20220705";              //���������Ϣ
    EVP_MD_CTX_init(ctx);                    //��ʼ��ժҪ�ṹ��
    EVP_DigestInit_ex(ctx, EVP_sm3(), NULL); //����ժҪ�㷨�������㷨���棬���������㷨ʹ��sm3���㷨����ʹ��OpenSSLĬ�����漴���㷨
    EVP_DigestUpdate(ctx, msg1, strlen(msg1));//����ժҪUpDate����msg1��ժҪ
    EVP_DigestFinal_ex(ctx, output, &len);//ժҪ���������ժҪֵ   
    EVP_MD_CTX_reset(ctx);                       //�ͷ��ڴ�

    printf("%s��hash:\n", msg1);
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
