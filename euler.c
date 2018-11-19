#include "stdio.h"
#include "stdlib.h"
#include "euler.h"

#define MAX_CELLS 1024
#define SUCCESS 0
#define FAIL 1

// euler.c - основной модуль
// stdio.h - заголовочный модуль.
// int - целое число 64
// unsigned int - цел число без знака.
// double - число с плав запятой с двойной точностью.
// float - число с плав запятой.

double result[MAX_CELLS];
int idx = 0;


int start_temperature_input() {
  return 100;
}

double f(double t, double T,
         double k, double Tenv) {
  return -k*(T-Tenv);
}

int simple_euler(double T0,
                 double Tenv,
                 double k,
                 double tend,
                 double h) {
  double T = T0, t=0.0;
  int i=0;
  int st = (int) 1/h; // отбросить дробную часть
  double dT;

  while (t<=tend) {
    if (i % st == 0) {
      if (idx>=MAX_CELLS) {
        fprintf(stderr, "FATAL: too few cells.\n");
        exit(FAIL);
      }
      result[idx]=T;
      idx++;
    }
    dT = f(t,T, k,Tenv)*h;
    T = T + dT;
    i++;
    t+=h; // t = t + h
  }
  return SUCCESS;
}

void output_as_table(double arr[],
                     int len) {
  int i;
  for (i=0;i<len;i++) {
    printf("%3i %f\n", i, arr[i]);
    // i++
  }
}

#ifndef COOL_MODULE
int main() {
  double T0 = start_temperature_input();
  double Tenv = 24;
  double h = 0.01;
  double tend = 60.0;
  double k = 0.01;
  int len;
  int rc = simple_euler(T0,Tenv,k,tend,h);
  len = idx;
  output_as_table(result,len);
  return SUCCESS;
}
#endif
