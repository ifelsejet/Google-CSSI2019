let firstName = "Jet";
let lastName = "Montes";
let age = 27;

//const for functions, let is bad practice
/*
FUNCTION FORMAT
const functionName = () => {

}
*/

//Function to determine if you can drive
const canYouDrive = (personAge) => {
  if(personAge >= 18){
    return "You can get a license!";
    /*
    if(firstName === "Jet"){
      console.log("You already have one!!")
    }
    */
  }
  else if (personAge >= 16) {
    return "You can get a permit!";
  }
  else if(personAge >= 8){
    return "Don't drive!";
  }
  else {
    return "What are you doing???";
    //console.log('Don\'t drive!');
  }
};

/*
console.log(firstName + ' ' + lastName);
console.log(123);
console.log("hehe");
*/

// == non=strict equality
// === Strict equality

/*
if(age >= 18){
  console.log("You can get a license!");
  if(firstName === "Jet"){
    console.log("You already have one!!")
  }
}
else if (age >= 16) {
  console.log("You can get a permit!")
}
else {
  console.log("Don't drive!!!!!!!!!!!!!");
  //console.log('Don\'t drive!');
}
*/
