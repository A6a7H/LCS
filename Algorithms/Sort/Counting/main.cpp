 #include <iostream>
#include <fstream>

int findMax(int *numbers, int array_size) {
    int max = INT32_MIN;
    for (int i =0; i<array_size; ++i)
        if (numbers[i]>max)
            max = numbers[i];
    return max;
}

int findMin(int *numbers, int array_size) {
    int min = INT32_MAX;
    for (int i =0; i<array_size; ++i)
        if (numbers[i]<min)
            min = numbers[i];
    return min;
}

void countingSort(int *numbers, int array_size)
{
    int max = findMax(numbers,array_size);
    int min = findMin(numbers,array_size);
    int* helper = new int[max-min+1];
    int* result = new int[array_size];
    for (int i=0;i<max-min+1;++i){
        helper[i] = 0;
    }
    for (int i=0;i<array_size;++i){
        helper[numbers[i]-min]++;
    }
    for (int i=1;i<max-min+1;++i){
        helper[i] += helper[i-1];
    }
    for (int i=array_size-1;i>=0;--i){
        helper[numbers[i]-min]--;
        result[helper[numbers[i]-min]] = numbers[i];
    }
    for (int i=0;i<array_size;++i){
        numbers[i] = result[i];
    }
    delete[] result;
    delete[] helper;
}

int main() {

    std::fstream fin;
    std::fstream fout;

    fin.open("input.txt", std::ios::in);
    fout.open("output.txt", std::ios::out);

    int *brr = nullptr;
    int n =0 ;
    //Ввод из файла
    fin >> n;
    brr = new int[n];
    for (int i=0; i<n; ++i)
        fin >> brr[i];
    fin.close();
    //Запуск сортировки, ответ в том же массиве (brr)
    countingSort(brr, n);
    //Запись в файл
    for (int i=0; i<n; ++i)
        fout << brr[i] << " ";

    fout.close();
    delete[] brr;
    return 0;
}