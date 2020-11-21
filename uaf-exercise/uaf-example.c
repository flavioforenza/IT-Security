#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

struct auth {
  char name[32];
  int auth; //1 login
};

struct auth *auth;
char *service;

//OBBIETTIVO: cambiare il valore della variabile auth con il valore 1
//N.B: notare che non vi è nessuna parte che cambia auth per impostarlo a 1
//N.B: non è possibile fare un BOF
int main(int argc, char **argv)
{
  char line[128];

  while(1) {
      //stampa dei puntatori di auth e service
      printf("[ auth = %p, service = %p ]\n", auth, service);
      //lettura da stdin con scrittura in line
      //N.B: non si può scrivere oltre la dimensione di line sizeof(line)==> NO BOF
      if(fgets(line, sizeof(line), stdin) == NULL) break;
      
      //4 CASI:
      //1
      if(strncmp(line, "auth ", 5) == 0) {
          //malloc di auth
          auth = malloc(sizeof(auth));
          //inizializza auth con diversi 0
          memset(auth, 0, sizeof(auth));
          //controllo lunghezza auth
          if(strlen(line + 5) < 31) {
 	      //copio il nome in name (auth admin)
              strcpy(auth->name, line + 5);
          }
      } 
      //2
      if(strncmp(line, "reset", 5) == 0) {
          //libera la memoria puntata da auth
          free(auth);
      }
      //3
      if(strncmp(line, "service", 6) == 0) {
          //implicitamente effettua una malloc della stringa successiva a service (es: hack)
          //service ha già un puntatore
          service = strdup(line + 7);
      }
      //4
      if(strncmp(line, "login", 5) == 0) {
	  //se auth = 1
          //Qui sta la vulnerabilità UAF. L'if accede ad auth anche se è stato liberato
          if(auth->auth) {
              printf("you have logged in already!\n");
          } else {
              printf("please enter your password\n");
          }
      }
  }
 }
