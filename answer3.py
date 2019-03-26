nextFibonacci(array[]){
  x = 1;
  y = 1;
  a = 0;
  turn = 0;
  for(i = 0;i < array.length;i++ ){
    while(a == 0){
      if(turn = 0){
        x = x+y;
        turn++;
      }
      else if(turn=1){
        y=x+y;
        turn--;
      }
      
      if(x>=array[i]){
        print(x);
        a=1;
      }
      if(y>=array[i]){
        print(y);
        a=1;
      }
    }
  }
}
