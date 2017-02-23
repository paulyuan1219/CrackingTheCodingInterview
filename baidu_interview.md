## Feb 23 Baidu 1st phone interview

Dice  1 2 3 4 5 6
3 Times
Prob(sum is 5) 
=P(1,1,3)+P(1,2,2)
=3*(1/6)^3 + 3*(1/6)^3 

I cannot see anything here. Can you type it below.


Matrix indicating a maxe

>S 1 0 0
>0 1 0 0
>0 1 0 0
>0 0 0 E

1 means the grid blocked
0 means the grid is accessable

Given start and end point point, write a function to see if you can go from start to end

start: 0,0
end : 3,3
=> yes

int A[][]; // save the matrix

bool find_path_bfs_iterative(int sx int sy, int ex, int ey){ 
    // if s is next to e, we are here
    if(sx==ex && (sy==ey+1 || sy==ey-1)){
        return true;
    }
    if(sy==ey && (sx==ex+1 || sx==ex-1)){
        return true;
    }
    
    
    unvisited_list= unvisited_neighbours_of(sx,sy) // i.e. value == 0
    for each (x,y) in unvisited_list:
        set A[x,y]=2 // mark as visited
        
    while(unvisited_list is not empty){
        current_pos = unvisited_list.pop(0); // pop out the first element.
        
        if(current_pos is next to (ex,ey)):
            return true;
        else:
            unvisited_list.extend(unvisited_neighbours_of_current_pos)
    }
    
    return false;
}    
   


bool find_path(int start_x, int start_y, int end_x, int end_y){ 

    // assert that start_x, start_y, end_x, end_y are valid, i.e. >=0 <N

    bool result = bfs(start_x, start_y, end_x, end_y);

    return result;

}


bool bfs(start sx, start sy, end ex, end ey){
    // if s is next to e, we are here
    if(sx==ex && (sy==ey+1 || sy==ey-1)){
        return true;
    }
    if(sy==ey && (sx==ex+1 || sx==ex-1)){
        return true;
    }
    
    // look s's neighbors
    unvisited_list = s's unvisited neighbors // check all surranding neighours with value == 0.
    
    if (unvisited_list is empty)
        return false;
        
    bool result = false;
    for each positiion (x,y) in unvisisted_list:
    {
        A[x,y]=2; // indicate it is visited
        result = bfs(x,y, ex, ey);
        if(result){
            return true;
        }
    }    
    return result;  

}


１，behavior question
２，实现一个c++的vector<T>以及　iterator
３，不确定长度的有序数组找数
４，一个很大的list<object>, 每一object有１Ｍ大小，内存放不下，用户如何查询
５，概率统计
