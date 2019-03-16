#include <iostream>
#include <string>
#include "queue"
#include "ReadWriter.h"

using namespace std;

bool comp(const Edge& l, const Edge& r)
{
    return l.W > r.W;
}
//Основной метод решения задачи, параметры:
//N - количество вершин, M - количество ребер в графе
//edges - вектор ребер, каждое ребро представлено 3-мя числами (А,В,W), где A и B - номера вершин, которые оно соединяет, и W - вес ребра,
//передается по ссылке (&), чтобы не копировать, изменять вектор и его значения можно.
//Результат также в виде вектора ребер, передается по ссылке (&), чтобы не копировать его.
void solve(int N, int M, vector<Edge>& edges, vector<Edge>& result)
{
    vector<vector<Edge>> sm_grapth(N);
    for (int i = 0; i < M; ++i){
        sm_grapth[edges[i].A].push_back(edges[i]);
        sm_grapth[edges[i].B].push_back(edges[i]);
    };
    vector<bool> visited(N, false);
    auto cmp = [](const Edge& a, const Edge& b)
    {
        return a.W > b.W;
    };
    priority_queue<Edge, vector<Edge>, decltype(cmp)> Q(cmp);
    for (int i = 0; i < sm_grapth[0].size(); ++i)
        Q.push(sm_grapth[0][i]);
    visited[0] = true;
    while ( !Q.empty() ) {
        Edge v = Q.top();
        Q.pop();
        int check = visited[v.A] ? v.B : v.A;
        if (!visited[check]) {
            result.push_back(v);
            visited[check] = true;
            for (int i = 0; i < sm_grapth[check].size(); ++i) {
                Q.push(sm_grapth[check][i]);
            }
        }
    }
}


int main()
{
    ReadWriter rw;
    //Входные параметры
    //N - количество вершин, M - количество ребер в графе
    int N, M;
    rw.read2Ints(N, M);

    //Вектор ребер, каждое ребро представлено 3-мя числами (А, В, W), где A и B - номера вершин, которые оно соединяет, и W - вес ребра
    //Основной структурой выбран вектор, так как из него проще добавлять и удалять элементы (а такие операции могут понадобиться).
    vector<Edge> edges;
    rw.readEgdes(M, edges);

    //Основной структурой для ответа выбран вектор, так как в него проще добавлять новые элементы.
    //(а предложенные алгоритмы работают итеративно, увеличивая количество ребер входящих в решение на каждом шаге)
    vector<Edge> result;

    //Алгоритм решения задачи
    //В решение должны входить ребра из первоначального набора!
    solve(N, M, edges, result);

    //Выводим результаты
    rw.writeInt(result.size());
    rw.writeEdges(result);

    return 0;
}