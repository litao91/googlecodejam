#include<list>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>

int count = 0;
void read_problem(int** vals, int* cnt, int* sum,  char* filename){
    FILE *fp = fopen(filename, "r");
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    if(fp == NULL) {
        exit(EXIT_FAILURE);
    }

    getline(&line, &len, fp);
    *cnt = atoi(line);
    *vals = new int[*cnt];
    char* pch;

    getline(&line, &len, fp);
    pch = strtok(line, " ");
    int i = 0;
    while(pch!= NULL) {
        (*vals)[i] = atoi(pch);
        i++;
        pch=strtok(NULL, " ");
    }
    getline(&line, &len, fp);
    *sum = atoi(line);
}

int sum_arr(int* arr, int cnt){
    int sum = 0;
    for(int i = 0; i<cnt; i++) {
        sum+= arr[i];
    }
    return sum;

}

void solve_problem(const int* vals, int** picks, int** m_picks,  int sum, int cnt) {
    if(cnt == 0) {
        for(int i = 0; i < count; i++) {
            printf("%d", (*picks)[i]);
        }
        printf("\n");
        if( sum == 0) {
            if(sum_arr(*picks, count) < sum_arr(*m_picks,count)) {
                for(int i = 0; i < count; i++) {
                    (*m_picks)[i] = (*picks)[i];
                }
            }
        }
        return;
    }

    int max_pick = sum/vals[cnt-1];
    for(int j = max_pick; j>=0; j--) {
        (*picks)[cnt-1] = j;
        solve_problem(vals, picks, m_picks, sum-vals[cnt-1]*j, cnt-1);
    }
}

int main(int argc, char** argv) {
    int* vals = NULL;
    int cnt;
    int sum;
    read_problem(&vals, &cnt, &sum, argv[1]);
    count = cnt;
    int* temp = new int[cnt];
    int* picks = new int[cnt];
    for(int i = 0; i < cnt; i++) {
        picks[i] = INT_MAX;
    }

    solve_problem(vals,  &temp, &picks,  sum, cnt);

    for(int i = 0; i < cnt; i++) {
        printf("%d ", picks[i] );
    }
    printf("\n");

    delete[] picks;
    delete[] vals;
    delete[] temp;
}

