#include <stdio.h>
int main()
{
    char *a="A string";
    printf("%c %d t\n",*a,a);
    a+=2;
    printf("%d %c %c",a,*(a+2),*(a+5));
    return 0;
}
