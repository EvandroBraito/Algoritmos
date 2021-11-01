#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>

int randomizador_de_cor(x, y)
{
    if (y == 1)
        return rand() % 8 + 1;

    if (y == 12)
        return rand() % 8 + 1;

    if (x == 1)
        return = rand() % 8 + 1;

    if (x == 40)
        return rand() % 8 + 1;
}

void selecionador_de_cores(dx, dy, colors)
{
    if (dx == 1 && dy == -1)
        return_textcolor(colors);

    if (dx == 1 && dy == 1)
        _textcolor(colors);

    if (dx == -1 && dy == -1)
        _textcolor(colors);

    if (dx == -1 && dy == 1)
        _textcolor(colors);
}

int fisica_bolinha_x(int x, int dx)
{
    if (x == 1 || x == 40)
        dx = -dx;

    return dx;
}

int fisica_bolinha_y(int y, int dy)
{
    if (y == 1 || y == 12)
        dy = -dy;

    return dy;
}

int main(void)
{
    int x = 1, y = 1, dx = -1, dy = -1;
    int colors;

    do
    {
        colors = randomizador_de_cor(x, y);

        _gotoxy(x, y);
        printf("O\b");
        _sleep(1);
        printf("*");

        dx = fisica_bolinha_x(x, dx);
        dy = fisica_bolinha_y(y, dy);

        selecionador_de_cores(dx, dy, colors);

        x += dx;
        y += dy;

    } while (!_kbhit());

    return 0;
}
