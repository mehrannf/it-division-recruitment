# Questions

## Question 1

What is the time complexity of the following C program?

```c
#include <stdio.h>

#define MAXN 100

int main() {
    int n = 0, i = 0, j = 0;
    int mat[MAXN][MAXN];

    fscanf(stdin, "%d", &n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            fscanf(stdin, "%d", &mat[i][j]);
        }
    }

    for (i = 0; i < n; i++) {
        mat[i][0] *= 2;
    }
}
```

## Question 2

What is a memory leak? Explain how to correctly free memory after a dynamic
memory allocation in C

## Question 3

What is an abstract method in OOP? How is it used?

## Question 4

How is `systemd` used in most Linux systems?

## Question 5

What is a `git rebase`?