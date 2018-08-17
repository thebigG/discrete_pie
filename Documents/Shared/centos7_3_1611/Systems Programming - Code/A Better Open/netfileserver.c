/****************** SERVER CODE ****************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <netdb.h>
#define LOCAL_HOST "12.0.0.1"
#define PORT "9004"
int main(int argc, char** argv){
  int welcomeSocket, newSocket;
  char buffer[1024];
  struct addrinfo hints ;
  struct addrinfo *res;
  //socklen_t addr_size;
// res = malloc(sizeof(struct addrinfo*));
// *res = malloc(sizeof(struct addrinfo));
//*res->
  /*---- Create the socket. The three arguments are: ----*/
  /* 1) Internet domain 2) Stream socket 3) Default protocol (TCP in this case) */
  welcomeSocket = socket(PF_INET, SOCK_STREAM, 0);

  /*---- Configure settings of the server address struct ----*/
  /* Address family = Internet */
   hints.ai_family = AF_INET;
   hints.ai_socktype  = SOCK_STREAM;
  // /* Set port number, using htons function to use proper byte order */
  // serverAddr.sin_port = htons(9000);
  // /* Set IP address to localhost */
  // serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
  printf("Running address info...\n");
  memset(&hints, 0, sizeof(struct addrinfo));
 if(getaddrinfo(NULL, PORT, &hints, &res )!=0)
 {
   perror("There was a problem with getaddrinfo");
   return -1;
 }
  /* Set all bits of the padding field to 0 */

  /*---- Bind the address struct to the socket ----*/
  if( (bind(welcomeSocket,  res->ai_addr, (res->ai_addrlen))) !=0)
  {
    perror("bind");
  }

  /*---- Listen on the socket, with 5 max connection requests queued ----*/
  if(listen(welcomeSocket,5)==0)
  printf("Listening\n");
  else
  printf("Error\n");

  /*---- Accept call creates a new socket for the incoming connection ----*/
  //addr_size = sizeof serverStorage;
  newSocket = accept(welcomeSocket, res->ai_addr, &res->ai_addrlen);
  //create thread, probably
  if(newSocket!=0)
  perror("Accept");

  /*---- Send message to the socket of the incoming connection ----*/
  strcpy(buffer,"Hello World\n");
  send(newSocket,buffer,13,0);

  return 0;
}
