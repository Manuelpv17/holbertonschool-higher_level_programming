#include "hash_tables.h"
/**
 * hash_djb2 - implementation of the djb2 algorithm
 * @str: string used to generate hash value
 *
 * Return: hash value
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int i;

	hash = 5381;
	for (i = 0; str[i] != '\0'; i++)
		hash = ((hash << 5) + hash) + str[i];

	return (hash);
}
