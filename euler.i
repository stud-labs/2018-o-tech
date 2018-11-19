 /* euler.i */
 %module euler
 %{
#include "euler.h"
#include "stdio.h"
#include "stdlib.h"
 %}

void output_as_table(double arr[], int len);

int simple_euler(double T0,
                 double Tenv,
                 double k,
                 double tend,
                 double h);
