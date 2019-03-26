#include <stdio.h>
#include <string.h>


string isSubset(char A[26],char B[26]){
  int count = 0;
  for(int i = 0; i < sizeof(B) ; i++){
    for(int j =0; j < sizeof(A); j++){
      if(A[j] != B[i])count++;
    }
  }
  if(count == 0) return "True";
  else return "False";
  count = 0;
}

int main()
{
    char A['a','b,'c'];
    char B['b','c'];
    isSubset(A,B);
    return 0;
}
