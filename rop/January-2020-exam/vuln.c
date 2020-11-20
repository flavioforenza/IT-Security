#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>


char string[100] ;

char str1[5] ;
char str2[4] ;

void join_string(char *dst, char *src) 
{
	strcat(dst, src) ;
}

void lazy() 
{
	execve(string, 0, 0) ;
}



void get_input()
{
  //*buf is in libc --> NULL (necessary return 0x0a)
  char *buf = NULL ;
  char buffer[128];
  char buffer1[20] ;

  /* get buffer */
  gets(buffer);

  /* get input */
  //strncpy(#dest, source, nbytesToCopy)
  if (buf != NULL) strncpy(buf, buffer, 5) ;

  /* get buffer1 */
  gets(buffer1);

  /* get input */
  if (buf != NULL) strncpy(buf, buffer1, 4) ;

}

int main(int argc, char **argv)
{
  

 get_input() ; 
  
  
}
