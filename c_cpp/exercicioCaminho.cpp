#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{

    int col = 40, lin = 12;
    int rastro = 219;
    int rastro_troca = 0;
    int colors = 2;

    while (1)
    {

        _gotoxy(col, lin);
        _putch(rastro);

        switch (toupper(_getch()))
        {
        case 'N':
            if (lin > 1)
                lin--;
            break;
        case 'S':
            if (lin < 24)
                lin++;
            break;
        case 'L':
            if (col < 80)
                col++;
            break;
        case 'O':
            if (col > 1)
                col--;
            break;
        case 'R':
            if (rastro_troca == 0)
            {
                rastro = 0;
                rastro_troca = 1;
            }
            else if (rastro_troca == 1)
            {
                rastro = 219;
                rastro_troca = 0;
            }
            break;
        case 'C':
            _textcolor(colors++);
            if (colors >= 15)
                colors = 2;
            break;
        case 'F':
            exit(1);
        }
    }
    return 0;
}
