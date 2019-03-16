#include <iostream>
#include <fstream>
#define osnovanie 256


union UN
{
    unsigned int a;
    unsigned char b[4];
};


void countSort(UN *numbers, int array_size, int exp){
    unsigned int count[256];
    for (int i = 0; i < 256; ++i)
    {
        count[i] = 0;
    }
    UN output[array_size];

    for (int i = 0; i < array_size; i++)
        count[numbers[i].b[exp]]++;

    for (int i = 1; i < 256; i++)
        count[i] += count[i - 1];

    for (int i = array_size-1; i >=0 ; i--)
    {
        count[numbers[i].b[exp]]--;
        output[count[numbers[i].b[exp]]].a = numbers[i].a;
    }
    for (int i = 0; i < array_size; i++)
        numbers[i].a = output[i].a;
}

void radixSort(UN *numbers, int array_size)
{
    for (int i=0;i<4; i++){
        countSort(numbers,array_size,i);
    }
}

int main() {

    std::fstream fin;
    std::fstream fout;

    fin.open("input.txt", std::ios::in);
    fout.open("output.txt", std::ios::out);

    UN *brr = nullptr;
    int n =0 ;
    //Ввод из файла
    fin >> n;
    brr = new UN[n];
    for (int i=0; i<n; ++i)
        fin >> brr[i].a;
    fin.close();
    //Запуск сортировки, ответ в том же массиве (brr)
    radixSort(brr, n);
    //Запись в файл
    for (int i=0; i<n; ++i)
        fout << brr[i].a << " ";

    fout.close();
    delete[] brr;
    return 0;
}