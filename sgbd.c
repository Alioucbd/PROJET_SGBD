#include <stdio.h>
#include <string.h>
#include <libxml/parser.h>


int main(int argc, char const *argv[])
{
	
	if (xmlParseFile(argv[1])==NULL)
	{
		printf(" format xml non respecte\n");
	}else{
		printf(" fichier xml valide\n");
	}
	return 0;
}