#include<stdio.h>

int main(){
    FILE *stream = fopen("input/input1.txt", "r");
    char  bandit[100];
    char s1[100];
    char test[100];
    int n1;
    int n;
    int i;
    int j;
    int flag =1;
    
    if (stream == NULL){
        printf("non stampa un cazzo\n");
    }
    else
        fscanf(stream,"%d %d", &n, &n1);
        printf("%d %d   \n", n, n1);
        fgets(bandit, 100, stream);

        //trovo le parole bandite
        for(i =1; i<n1+1; i++){
            fgets(bandit, 100, stream);
            printf(" bandit= %s.\n", bandit);
        }

        int p =0;

        //corrro e getto tutte le parole della lista
        for(j =i; j<n; j++){
            fgets(test, 100, stream);
            p =0;
            flag = 1;
            printf("parola = %s\n", test);
            //confronto le parole lettera per lettera
            while(test[p] != "\0" && flag){
                printf("test[p] = %c\n", test[p]);
                if(bandit[p] == test[p]){
                    p++;
                }
                else{
                    flag =0;
                    printf("SECURE\n");
                }
            }
            if (flag){
                printf("BANNED\n");

            }
            
        
        }


   /*
   
   */

    return 0;
}