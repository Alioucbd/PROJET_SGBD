#include <stdio.h>
#include <string.h>
#include <libxml/parser.h>

int
main(int argc, char **argv)
{
    xmlDoc         *document;
    xmlNode        *root, *first_child, *node;
    char           *filename;
    xmlChar        *  val;     
    xmlNode *cur_node = NULL;

    if (argc < 2) {
        fprintf(stderr, "Usage: %s filename.xml\n", argv[0]);
        return 1;
    }
    filename = argv[1];
    document = xmlReadFile(filename, NULL, 0);
    //doc =xmlParseFile(filename);
	if (document==NULL)
	{
		printf(" format xml non respecte\n");
	}else{
		printf(" fichier xml valide\n");
	}

    
    root = xmlDocGetRootElement(document);

    fprintf(stdout, "Root is <%s> (%i)\n", root->name, root->type);
    first_child = root->children;

    for (node = first_child; node; node = node->next) {
        
        val= xmlNodeGetContent(cur_node);
        fprintf(stdout, "\t Child is <%s> (%i)\n", node->name, node->type);
    }
    
    fprintf(stdout, "...\n");
    xmlFreeDoc(document);
    return 0;
}
