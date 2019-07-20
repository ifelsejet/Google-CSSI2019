//array, essentially a Java arrayList
const headerName = document.querySelector("#header");
const theButton = document.querySelector("#buttonID");
let people = ['Logan', 'Ciera', 'Rachel'];

let students = ['Asia', 'Daniela', 'Tjay'];
console.log("First element is " + people[0]);
console.log("Second element is " + people[1]);

//people[1] = "Rachel";
//.push() is to push something onto the end of the array
people.push("Foo");

//pop() is to remove something from the end of the array
people.pop();
//.length is array length, always one more than the last index of an array
console.log(people);
console.log("length is: " + people.length);

let everyone = people.concat(students);

//randomNumber between 0-1
//floor cuts off the decimals

theButton.addEventListener('click', () =>{
  let randomIndex = Math.floor(Math.random() * everyone.length);
  headerName.innerHTML = everyone[randomIndex];
  console.log(randomIndex);
});


/*.join() adds something between each element in an array
indexOf returns the index of an element within an array
if NOT found, returns -1.
.concat adds everything from two arrays and "drops it on the floor", could be
assigned to a variable
people.concat(students);
*/
