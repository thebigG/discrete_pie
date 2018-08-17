#include<stdlib.h>
#include<stdio.h>
#include <fcntl.h>
int netopen(const char *pathname, int flags)
{

int file  =   open(pathname, flags);
if(file == -1)
{ 
perror("There was a problem opening this file");
return -1;
}
printf("netopen was a success!\n");
close(file);
return 0;
}
int netserverinit(const char *hostname)
{
  struct addrinfo hints ;
  struct addrinfo **res;
}
