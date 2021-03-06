var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = temp;
};
var indexOfMinimum = function(array, startIndex) {
    // Set initial values for minValue and minIndex,
    // based on the leftmost entry in the subarray:  
    var minValue = array[startIndex];
    var minIndex = startIndex;
    for(var i = minIndex + 1; i < array.length;i++){
        if(array[i]<minValue){
            minIndex = i;
            minValue = array[i];
        }
    }    
    // Loop over items starting with startIndex, 
    // updating minValue and minIndex as needed:
    
    return minIndex;
}; 


var selectionSort = function(array) {
    var length = array.length;
    for(var i = 0; i < length; i++){
        var min = indexOfMinimum(array,i);
        swap(array, i, min);
    }

};

var array = [18, 6, 66, 44, 9, 22, 14];   
var index = indexOfMinimum(array, 2);

//  For the test array [18, 6, 66, 44, 9, 22, 14], 
//  the value 9 is the smallest of [..66, 44, 9, 22, 14]
//  Since 9 is at index 4 in the original array, 
//  "index" has value 4
println("The index of the minimum value of the subarray starting at index 2 is " + index + "."  );
Program.assertEqual(index, 4);
Program.assertEqual(indexOfMinimum([2,3,4,5,1], 4),4);
Program.assertEqual(indexOfMinimum([2,2,4,5,2,1], 1),5);
