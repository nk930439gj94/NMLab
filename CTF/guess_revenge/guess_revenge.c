#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void win() {
  FILE *flag;
  char *buf = NULL;
  size_t len = 0;
  flag = fopen("/home/joey/Desktop/hw/flag.txt", "r");
  getline(&buf, &len, flag);
  printf("%s\n", buf);
}

int main() {
  srand(time(NULL));
  int answer = rand();
  char guess[15];
  for(int i=0;i<100;i++) {
    printf("Input: ");
    fflush(stdout);
    fgets(guess, 15, stdin);
    if(atoi(guess) == answer && answer == 20202020) {
      win();
    }
    else {
      printf(guess);
      printf(" is not correct!\n");
    }
  }
  return 0;
}