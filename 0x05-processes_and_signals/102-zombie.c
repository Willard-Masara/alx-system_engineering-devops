#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to keep the program running.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
	sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t zombie_pid;

	/* Create 5 zombie processes*/
	for (int i = 0; i < 5; i++)
	{
	zombie_pid = fork();

	/* Child process */
	if (zombie_pid == 0)
	{
	    
	    printf("Zombie process created, PID: %d\n", getpid());
	    exit(0);
	}
	}

	infinite_while();
	return (0);
}

