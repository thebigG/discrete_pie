/****************** CLIENT CODE ****************/

#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include<stdlib.h>
#include <netdb.h>
#include <sys/uio.h>
#include <unistd.h>
#include<err.h>

//#define LOCAL_HOST "1.77777.12"
#define PORT "9004"

int main(int argc, char** argv)
{
  if(argc!=2)
  {
  printf("No enough arguments to connect to server\n");
  return -1;
  }
  char* ServerName  = malloc((sizeof(char)* strlen(argv[1])) + 1);
  int clientSocket = 0;
  char *buffer =  malloc(sizeof(char) * 256);
  struct addrinfo hints;
  struct addrinfo* SocketInfo;
  //socklen_t addr_size;
  strcpy(ServerName, argv[1]);
  printf("Server name: %s\n", ServerName);
  /*---- Create the socket. The three arguments are: ----*/
  /* 1) Internet domain 2) Stream socket 3) Default protocol (TCP in this case) */
  //clientSocket = socket(PF_INET, SOCK_STREAM, 0);
  /*---- Configure settings of the server address struct ----*/
  /* Address family = Internet */
  // serverAddr.sin_family = AF_INET;
  // /* Set port number, using htons function to use proper byte order */
  // serverAddr.sin_port = htons(9001);
  // /* Set IP address to localhost */
  // serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
  /* Set all bits of the padding field to 0 */
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_INET;
  hints.ai_socktype  = SOCK_STREAM;
  //memset(serverAddr.sin_zero, '\0', sizeof (serverAddr.sin_zero));
  int error = getaddrinfo(ServerName, PORT, &hints, &SocketInfo );
  if(error)
  {
    errx(1, " gteaddrinfo: %s", gai_strerror(error));
    return -1;
  }
  struct addrinfo  p;
  //p = SocketInfo;
  // for(p = SocketInfo;p!= NULL; p =  p->ai_next)
  // {
  //   if( (clientSocket = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1)
  //   {
  //     perror("socket");
  //     continue;
  //   }
  //   if(connect(clientSocket, (struct sockaddr*)p->ai_addr,(socklen_t) p->ai_addrlen) != -1)
  //   {
  //       close(clientSocket);
  //       perror("connect");
  //       break;
  //   }
  //   continue;
  // }
  /*---- Connect the socket to the server using the address struct ----*/
  //addr_size = sizeof serverAddr;
  // if(p == NULL)
  // {
  //   fprintf(stderr, "There was a problem connecting to this server\n");
  //   return -1;
  // }

  /*---- Read the message from the server into the buffer ----*/
  if( (clientSocket = socket(SocketInfo->ai_family, SocketInfo->ai_socktype, SocketInfo->ai_protocol)) == -1)
   {
     perror("socket");
//     continue;
	return -1;
   }
     if(connect(clientSocket, SocketInfo->ai_addr,(socklen_t) SocketInfo->ai_addrlen) == -1)
     {
         close(clientSocket);
          perror("connect");
          return -1;
    }
  int bytes =  read(clientSocket, buffer, 14);
  if(bytes == -1)
  perror("read");
printf("socket file descriptor: %d\n",clientSocket );
  /*---- Print the received message ----*/
  printf("Data received: %s and read %d bytes\n",buffer, bytes);

  return 0;
}
