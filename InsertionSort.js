//Before the insert function is called:
//* the elements from array[0] to array[rightIndex] are sorted in ascending order.

//After calling the insert function:
//* value and the elements that were previously in array[0] to array[rightIndex], should be sorted in ascending order and stored in the elements from array[0] to array[rightIndex+1].

var insert = function(array, rightIndex, value) {
    for(var j = rightIndex;
          j >= 0 && array[j] > value;
          j--) {
          array[j + 1] = array[j];
      }   
      array[j + 1] = value; 
};

var insertionSort = function(array) {
    for (var st = 1; st < array.length; st++) {
    insert(array, st - 1, array[st]);
    }
};

var array = [3, 5, 7, 11, 13, 2, 9, 6];

insert(array, 4, 2);
println("Array after inserting 2:  " + array);
//Program.assertEqual(array, [2, 3, 5, 7, 11, 13, 9, 6]);

insert(array, 5, 9);
println("Array after inserting 9:  " + array);
//Program.assertEqual(array, [2, 3, 5, 7, 9, 11, 13, 6]);

insert(array, 6, 6);
println("Array after inserting 6:  " + array);
//Program.assertEqual(array, [2, 3, 5, 6, 7, 9, 11, 13]);
