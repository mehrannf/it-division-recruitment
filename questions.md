# Questions

## Question 1

What is the time complexity of the following C program?
The nested "for" reades n \* n elements related to the O(n^2) , however the second loop change n elements and it is going to the O(n)
At last the overall time complexity is O(n^2).

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

A memory leak happens when a program allocates memory dynamically using malloc , calloc but its going to fail to free when it using it free().
in conclusion memory is no longer used stays reserved, leading to wasted resources and possible crashes in long running applications.

## Question 3

What is an abstract method in OOP? How is it used?

It is the method ddeclared without implementation in base class. there is also subclasses which is must override and implement it.
This is methods are used to enforce a common interface across different subcalasses

## Question 4

How is `systemd` used in most Linux systems?
This syntax in the linux is for service manager used in the most modern disturbutions. it is responsible for booting the system, managing services, logging and dependency handling.

## Question 5

What is a `git rebase`?

It is the commmand that moves or reapplies commits from one brance onto another.
it rewrites commit history to make it linear and cleaner.
This takes commits in feature and re-applies them in top of main.
Avoiding merge commits adn keeping the history tide.
