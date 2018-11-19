#include "stdio.h"
#include "stdlib.h"

/*
Тип данных (Data type) - идентификатор, определяющий
1. Представление значений [этого типа] в памяти ЭВМ,
2. Набор операций, которые можно выполнять со значенями [-"-].
3. Метаинфорамация значения.

int x=0;  // x - координата в декартовом пространстве.

      31                                 0
int 1. 01111111 11111111 11111111 11111111 - positive number
       11111111 11111111 11111111 11111111 - positive number
       -4 мрд до +4 мрд
    2. x+y, x-y, * **, (int) x, .....
    3.

float 1. int M, int Order     x=M*10^Order.
      2.
*/

typedef unsigned long int ulint;

/*
  Calculates factorial of n.
  `n` - a positive number or 0.
 */

ulint fact(ulint n) {
  if (n==0) return 1;
  else if (n==1) return 1;
  else return n * fact(n-1);
}

int main() {
  ulint n = 10;
  printf("Factorial of %lu is %lu\n", n, fact(n));
  return 0;
}
