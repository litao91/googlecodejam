#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#define GET_CELL(data, i, j, row_size) (data)[i*(row_size)+j]
#define ABS(val) ((val)>=0?(val):-(val))

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

void solve_problem(const int* blocks, int block_cnt, int** results){
    //Calculate the mean points
    int weight_sum = 0;
    double x_sum = 0;
    double y_sum = 0;
    for(int i = 0; i < block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, 4);
        int y1 = GET_CELL(blocks, i, 1, 4);
        int x2 = GET_CELL(blocks, i, 2, 4);
        int y2 = GET_CELL(blocks, i, 3, 4);
        double t_mid_x = ((double)(x1+x2))/2;
        double t_mid_y = ((double)(y1+y2))/2;
        int weight = (ABS(x1-x2)+1)*(ABS(y1-y2) + 1);
        weight_sum+= weight;
        x_sum += t_mid_x*weight;
        y_sum += t_mid_y*weight;
    }
    //printf("Sum(%f,%f)\n", x_sum, y_sum);
    double mid_x = x_sum/weight_sum;
    double mid_y = y_sum/weight_sum;
    //printf("mid (%f, %f)\n", mid_x, mid_y);
    //Find the nearest point to the mid
    int min_x = -1;
    int min_y = -1;
    int min_dist = -1;

    for(int i = 0; i<block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, 4);
        int y1 = GET_CELL(blocks, i, 1, 4);
        int x2 = GET_CELL(blocks, i, 2, 4);
        int y2 = GET_CELL(blocks, i, 3, 4);
        for(int x = x1; x <= x2; x++) {
            for(int y = y1; y <= y2; y++) {
                double d = ABS(mid_x-x)+ABS(mid_y-y);
                if(min_dist < 0 || d < min_dist) {
                    //printf("%f\n", d);
                    min_dist = d;
                    min_x = x;
                    min_y = y;
                }
            }
        }
    }

    int dist = 0;
    for(int i = 0; i<block_cnt; i++) {
        int x1 = GET_CELL(blocks, i, 0, 4);
        int y1 = GET_CELL(blocks, i, 1, 4);
        int x2 = GET_CELL(blocks, i, 2, 4);
        int y2 = GET_CELL(blocks, i, 3, 4);
        for(int x = x1; x <= x2; x++) {
            for(int y = y1; y <= y2; y++) {
                dist+= ABS(min_x-x)+ABS(min_y-y);
            }
        }
    }
    (*results)[0] = min_x;
    (*results)[1] = min_y;
    (*results)[2] = dist;
    //printf("(%d,%d,%d)\n", min_x, min_y, dist);
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
        int* result = new int[3];
        //for(int j = 0; j < block_cnt; j++) {
            //printf("in ln %d : (%d,%d,%d,%d)\n", j,
                    //GET_CELL(blocks, j,0,block_cnt),
                    //GET_CELL(blocks, j,1,block_cnt),
                    //GET_CELL(blocks, j,2,block_cnt),
                    //GET_CELL(blocks, j,3,block_cnt));
        //}
        solve_problem(blocks, block_cnt, &result);
        fprintf(outfile, "Case #%d: %d %d %d\n", i+1, result[0], result[1], result[2]);
        delete [] blocks;
        delete [] result;
    }

    if(line!=NULL) {
        free(line);
    }
    fclose(infile);
    fclose(outfile);
}
