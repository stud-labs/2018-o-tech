#ifndef __EULER_H__
#define __EULER_H__

void output_as_table(double arr[], int len);

int simple_euler(double T0,
                 double Tenv,
                 double k,
                 double tend,
                 double h);

#endif // __EULER_H__
