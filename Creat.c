#include <stdio.h>
#include <stdlib.h>
int main(){
FILE *fp;
fp=fopen("/tmp/fuckBitch.txt", "w+");
if(fp==NULL){
	printf("error\n");
	exit(0);
}
fprintf(fp,"stdc:%d\n",__STDC__);
fprintf(fp,"line:%d\n",__LINE__);
fprintf(fp,"date:%s\n",__DATE__);
fprintf(fp,"file:%s\n",__FILE__);
fprintf(fp,"time:%s\n",__TIME__);
fputs("i don\'t want to set the world on fire\n",fp);
fclose(fp);
return 0;
}
