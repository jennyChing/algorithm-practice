var factorial = function(n) {
    var result = 1;
    for(var i = 2; i<= n; i++) {
        result *= i;
    }
    return result;
};

println("The value of 5! should be " + 5*4*3*2*1);
println("The value of 5! is " + factorial(5));
println("The value of 0! should be 1");
println("The value of 0! is " + factorial(0));

//Program.assertEqual(factorial(5), 120);
//Program.assertEqual(factorial(0), 1);

//second approach

var factorial2 = function(n) {
	// base case: 
	if (n === 0){
	return 1;
	}
	// recursive case:
	return n*(factorial2(n-1));
}; 

println("The value of 0! is " + factorial(0) + ".");
println("The value of 5! is " + factorial(5) + ".");

Program.assertEqual(factorial(0), 1);
Program.assertEqual(factorial(5), 120);
