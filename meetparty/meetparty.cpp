#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <algorithm>
#define GET_CELL(data, i, j, row_size) (data)[i*(row_size)+j]
#define ABS(val) ((val)>=0?(val):-(val))
typedef long long ll;
using std::vector;
using std::iterator;
using std::pair;
using std::sort;
using std::lower_bound;
void read_problem(FILE*  fp, int* block_cnt, int** blocks ) {
    size_t len = 50;
    ssize_t bytes_read = 0;
    char* line = NULL;
    bytes_read =  getline(&line, &len, fp);
    if(bytes_read < 0) {
        puts("Error reading file\n");
        exit(EXIT_FAILURE);
    }
    *block_cnt = atoi(line);
    *blocks = new int[(*block_cnt)*4];
    if(line != NULL) {
        free(line);
    }
    line = NULL;
    for(int i = 0; i < *block_cnt; i++) {
        bytes_read = getline(&line, &len, fp);
        char* pch;
        pch = strtok(line, " ");
        int j = 0;
        while(pch!=NULL) {
            //printf("i = %d, j=%d, pos = %d, atoi=%d\n",i, j, i*(*block_cnt)+j, atoi(pch));
            GET_CELL(*blocks, i,j, 4) = atoi(pch);
            pch = strtok(NULL, " ");
            j++;
        }
        if(line!=NULL) {
            free(line);
            line = NULL;
        }
    }
}

void solve_problem(const int* blocks, int block_cnt, ll* results){
    //Calculate the mean points
    vector<pair<int,int> > v;
    vector<int> x;
    vector<int> y;
    for(int i = 0; i < block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, 4);
        int y1 = GET_CELL(blocks, i, 1, 4);
        int x2 = GET_CELL(blocks, i, 2, 4);
        int y2 = GET_CELL(blocks, i, 3, 4);
        //printf("%d %d %d %d\n", x1,y1,x2,y2);
        for(int ix = x1; ix <=x2; ix++) {
            for(int iy=y1; iy<=y2; iy++) {
                x.push_back(ix);
                y.push_back(iy);
                v.push_back(std::make_pair(ix,iy));
            }
        }
    }
    //sort x and y in order w.r.t. their position
    sort(x.begin(), x.end());
    sort(y.begin(),y.end());
    sort(v.begin(), v.end());
    vector<ll> sum_x;
    vector<ll> sum_y;
    sum_x.push_back(0);
    sum_y.push_back(0);
    for(int i = 0; i < v.size(); i++) {
        sum_x.push_back(sum_x.back()+x.at(i));
        sum_y.push_back(sum_y.back()+y.at(i));
    }

    ll min_cost = 1ll <<61;
    vector<pair<int, int> >::iterator it;
    pair<int, int> min_p;
    int n = v.size();
    for(it = v.begin(); it < v.end(); it++) {
        int pos_x = lower_bound(x.begin(), x.end(), it->first) - x.begin();
        int pos_y = lower_bound(y.begin(), y.end(), it->second) - y.begin();
        ll x_cost = ((ll)it->first)*(pos_x+1) - (ll)sum_x.at(pos_x+1) + //sum of the points at the left
            (ll)sum_x.back() - (ll)sum_x.at(pos_x+1) - (ll)((ll)it->first) * (n-pos_x-1);
        ll y_cost = ((ll)it->second)*(pos_y+1) - (ll)sum_y.at(pos_y+1) +
            (ll)sum_y.back() - (ll)sum_y.at(pos_y+1) - (ll)((ll)it->second) *(n-pos_y-1);
        ll cost = x_cost + y_cost;
        if(cost < min_cost) {
            min_cost = cost;
            min_p = *it;
        }
    }
    results[0] = min_p.first;
    results[1] = min_p.second;
    results[2] = min_cost;
}

int main(int argc, char** argv) {
    FILE* infile = fopen(argv[1],"r");
    FILE* outfile =fopen(argv[2],"w");
    char* line = NULL;
    size_t len = 10;
    getline(&line, &len, infile);
    int T = atoi(line);
    if(line!=NULL) {
        free(line);
        line = NULL;
    }
    //printf("T = %d\n", T);
    for(int i = 0; i< T; i++) {
        int block_cnt = 0;
        int* blocks = NULL;
        read_problem(infile, &block_cnt,  &blocks);
        ll* result = new ll[3];
        //for(int j = 0; j < block_cnt; j++) {
            //printf("in ln %d : (%d,%d,%d,%d)\n", j,
                    //GET_CELL(blocks, j,0,block_cnt),
                    //GET_CELL(blocks, j,1,block_cnt),
                    //GET_CELL(blocks, j,2,block_cnt),
                    //GET_CELL(blocks, j,3,block_cnt));
        //}
        solve_problem(blocks, block_cnt, result);
        fprintf(outfile, "Case #%d: %lld %lld %lld\n", i+1, result[0], result[1], result[2]);
        delete [] blocks;
        delete [] result;
    }

    if(line!=NULL) {
        free(line);
    }
    fclose(infile);
    fclose(outfile);
}
