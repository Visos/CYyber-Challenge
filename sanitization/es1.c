#include<stdio.h>
#include <string.h>
//size_t strcspn(const char *string1, const char *string2);


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
        printf("%d %d   ", n, n1);
        fgets(bandit,50, stream);   //solo per gettare la seconda riga

        //fgets(bandit,10, stream);   //solo per gettare la seconda riga
          //  printf("bandit= %s.", bandit);

        

        //trovo le parole bandite
        for(i =1; i<n1+1; i++){
            fgets(bandit, 50, stream);
        }
            printf("bandit= %s.", bandit);

 
        int p =0;
        


        //corrro e getto tutte le parole della lista
        for(i; i<n; i++){
            fgets(test, 50, stream);
            p =0;
            flag = 1;
            printf("%s=%s.\n", bandit,test);
            //confronto le parole lettera per lettera
            while((test[p] != "\0" || test[p] != "\n") && flag){
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