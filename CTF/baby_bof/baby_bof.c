#include <stdio.h>

int main() {
  char a[10];
  printf("a is located at %p\n", a);
  fflush(stdout);
  fgets(a, 55, stdin);
  return 0;
}
