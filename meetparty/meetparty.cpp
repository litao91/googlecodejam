#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#define GET_CELL(data, i, j, row_size) (data)[i*row_size+j]
#define ABS(val) (val>=0?val:-val)

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
            GET_CELL(*blocks, i,j, *block_cnt) = atoi(pch);
            pch = strtok(NULL, " ");
            j++;
        }
        if(line!=NULL) {
            free(line);
            line = NULL;
        }
    }
}

void solve_problem(const int* blocks, int block_cnt, int** results){
    //Calculate the mean points
    int weight_sum = 0;
    double x_sum = 0;
    double y_sum = 0;
    for(int i = 0; i < block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, block_cnt);
        int y1 = GET_CELL(blocks, i, 1, block_cnt);
        int x2 = GET_CELL(blocks, i, 2, block_cnt);
        int y2 = GET_CELL(blocks, i, 3, block_cnt);
        double mid_x = ((double)(x1+x2))/2;
        double mid_y = ((double)(y1+y2))/2;
        int weight = (ABS(x1-x2)+1)*(ABS(y1-y2) + 1);
        weight_sum+= weight;
        x_sum += mid_x*weight;
        y_sum += mid_y*weight;
    }
    double x_mid = x_sum/weight_sum;
    double y_mid = y_sum/weight_sum;
    printf("mid: (%f,%f)\n", x_mid, y_mid);
    //Find the nearest point to the mid
    int min_x = -1;
    int min_y = -1;
    int min_dist = -1;

    for(int i = 0; i<block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, block_cnt);
        int y1 = GET_CELL(blocks, i, 1, block_cnt);
        int x2 = GET_CELL(blocks, i, 2, block_cnt);
        int y2 = GET_CELL(blocks, i, 3, block_cnt);

    }
}

int main(int argc, char** argv) {
    FILE* infile = fopen(argv[1],"r");
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
        int* result = new int[3];
        solve_problem(blocks, block_cnt, &result);

        //for(int j = 0; j < block_cnt; j++) {
            //printf("(%d,%d,%d,%d)\n",
                    //GET_CELL(blocks, j,0,block_cnt),
                    //GET_CELL(blocks, j,1,block_cnt),
                    //GET_CELL(blocks, j,2,block_cnt),
                    //GET_CELL(blocks, j,3,block_cnt));
        //}
        delete [] blocks;
        delete [] result;
    }

    if(line!=NULL) {
        free(line);
    }
}
