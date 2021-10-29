/*
 *      Insertion Sort 
 * 
 *  algoritmo eficiente para ordenar um número pequeno de elementos.
 * 
 * Inicialização: O invariante de laço é válido antes da primeira iteração do laço, quando j = 1. 
 * Então, o subarranjo a[1 .. j − 1] consiste apenas no único elemento a[1], que é de fato o elemento
 * original em a[1]. Além disso, esse subarranjo é ordenado, e isso mostra que o invariantede
 * laço é válido antes da primeira iteração do laço.
 * O corpo do laço for funciona deslocando a[ j − 1], a[ j − 2], a[ j − 3], e assim por diante,
 * uma posição para a direita até encontrar a posição adequada para a[j]; nesse ponto ele insere o
 * valor de a[j]. Então, o subarranjo a[1 .. j] consiste nos elementos presentes originalmente em a[1 .. j],
 * mas em sequência ordenada. Portanto, incrementar j para a próxima iteração do laço for preserva o invariante de laço.
 * A condição que provoca o término do
 * laço for é que (j > a) ⋅ comprimento = n. Como cada iteração do laço aumenta j de 1, devemos ter j = n + 1 nesse
 * instante. Substituindo j por n + 1 no enunciado do invariante de laço, temos que o subarranjo a[1 .. n] consiste nos
 * elementos originalmente contidos em a[1 .. n], mas em sequência ordenada. Observando que o subarranjo a[1 .. n] é o
 * arranjo inteiro, concluímos que o arranjo inteiro está ordenado. Portanto o algoritmo está correto.
*/

#include <stdio.h>

void insertion_sort(int a[6])
{
    for (int chave, i, j = 1; j <= 5; j++)
    {
        chave = a[j];
        i = j - 1;
        while (i > -1 && a[i] > chave)
        {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = chave;
    }
}

int main(void)
{
    int a[6] = {5, 2, 4, 6, 1, 3};

    insertion_sort(a);

    for (int i = 0; i <= 5; i++)
    {
        printf("%d ", a[i]);
    }

    printf("\n");
    return 0;
}