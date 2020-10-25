#include <stdio.h>
#include <stdlib.h>

int* rotLeft(int a_count, int* a, int d, int* result_count) {

    *result_count = a_count;

    //We create an auxiliar array for copying the a rotate
    int *aux_array = malloc(sizeof(int)*a_count); 

    //We obtain the left rotations to be done if d > a_count
    d = d%a_count;
    
    int index;

    /*The idea is to copy from the number that its going to be the first one and 
    come back to the start when needed in order not to get a segmentation fault
    A visual example might be: (d = 4) [1, 2, 3, 4, 5] --1--> [2, 3, 4, 5, 1] --2--> [3, 4, 5, 1, 2] --3--> [4, 5, 1, 2, 3] --4--> [5, 1, 2, 3, 4]*/

    for (int i = 0; i < a_count; i++){   
        index = (d + i)%a_count;
        aux_array[i] = a[index];
    }

    a = aux_array;
    return a;
}

int main()
{   
    int size = 20;

    // We reserve the memory for the array
    int* a = malloc(size * sizeof(int));

    printf("The array before the left rotation is:");

    // We initialize the array
    for (int i = 0; i < size; i++) {
      *(a + i) = i + 1;
      printf(" %d", i + 1);
    }

    // The left rotation operator
    int d = 4;
    printf("\n");
    printf("The left rotation is: %d\n", d);

    int result_count;
    int* result = rotLeft(size, a, d, &result_count);

    printf("The array after the left rotation is:");

    for (int i = 0; i < result_count; i++) {
    printf(" %d", result[i]);
    }
}