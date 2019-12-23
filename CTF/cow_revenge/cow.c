#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const char* cow = "        \\   ^__^\n         \\  (oo)\\_______\n            (__)\\       )\\/\\\n                ||----w |\n                ||     ||";

void say(char* text) {
  int len = strlen(text);
  printf(" ");
  for(int i=0;i < len+2;i++) printf("_");
  printf(" \n< %s >\n ", text);
  for(int i=0;i < len+2;i++) printf("-");
  printf(" \n%s\n", cow);
  fflush(stdout);
}

void parse(char* buf, char* command) {
  int end_cmd = 0;
  int beg_text = 0;
  int len = strlen(buf);
  for(int i = 0;i < 7;i++) command[i] = (char)0;
  while(end_cmd < 7 && end_cmd < len-1) {
    if(buf[end_cmd] != (char)32) {
      command[end_cmd] = buf[end_cmd];
      end_cmd++;
    } else break;
  }
  beg_text = end_cmd;
  while(beg_text < len-1) {
    if(buf[beg_text] == (char)32) beg_text++;
    else break;
  }
  for(int i=0;i < len - beg_text;i++) buf[i] = buf[beg_text+i];
  buf[len-beg_text-1] = (char)0;
}

int main() {
  char buff[60];
  char command[7];
  char name[20] = "user";
  say("Hi! Commands: help, rename, echo, whoami, exit");
  while(true) {
    for(int i = 0;i < 60;i++) buff[i] = (char)0;
    printf(name);
    printf("> ");
    fflush(stdout);
    fgets(buff, 60, stdin);
    parse(buff, command);
    if(strcmp(command, "help") == 0) {
      say("Commands: help, rename, echo, whoami, exit");
    }
    else if(strcmp(command, "rename") == 0) {
      int len = strlen(buff);
      len = len > 19?19:len;
      for(int i = 0;i < len;i++) {
        name[i] = buff[i];
      }
      name[len] = (char)0;
      say("Sucess");
    }
    else if(strcmp(command, "echo") == 0) {
      say(buff);
    }
    else if(strcmp(command, "whoami") == 0) {
      say(name);
    }
    else if(strcmp(command, "exit") == 0) {
      break;
    }
    else {
      say("Invalid command");
    }
  }
  return 0;
}