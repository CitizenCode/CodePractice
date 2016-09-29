#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function declarations

int main(int argc, char * argv[]);
int * generate_array(int length);
void print_array(int * array, int length);
void terminate(int * array);

// Function implementations

int main(int argc, char * argv[]) {
    // Deal with args
    if (argc < 2) {
        printf("\nUSAGE: %s ARRAY_SIZE\n\n", argv[0]);
        return 1;
    }
    int length = atoi(argv[1]);

    // Header stdout
    printf("\n -- Quicksort --\n");
    printf("\nSorting an array of length %d\n", length);

    // Generate the array
    srand(time(NULL));
    int * array = generate_array(length);
    print_array(array, length);

    // Sort the array

    // All done
    terminate(array);

    return 0;
}

int * generate_array(int length) {
    int * array = malloc(sizeof(int)*length);
    for (int i = 0; i < length; i++) {
        array[i] = rand() % length;
    }
    return array;
}

void print_array(int * array, int length) {
    printf("\nArray contents: [");
    for (int i = 0; i < length - 1; i++) {
        printf("%d, ", array[i]);
    }
	printf("%d", array[length - 1]);
    printf("]\n");
}

void terminate(int * array) {
    free(array);
}
