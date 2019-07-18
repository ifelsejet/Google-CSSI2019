// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let currentlily = 1;

/* Use a querySelector to grab your frog from your HTML */;
const frogger = document.querySelector("#frog");

//Click to go to the next lilypad
frogger.addEventListener('click', () =>{
frogger.style.left = "33.5%";
frogger.style.top = "24%"});

//Make second lilypad glow once frog has moved on, once it
//has moved on, make first lilypad "de-glow"
const lPad1 = document.querySelector("#lilypad1");
const lPad2 = document.querySelector("#lilypad2");

frogger.addEventListener('click', () =>{
  lPad1.classList.remove("active");
  lPad2.classList.add("active");

});

//when mouse is over frog, increase size to 80px x 80px
 frogger.addEventListener('mouseover', () => {
   frogger.style.height = "80px";
   frogger.style.width = "80px";
 });

//when mouse is not over frog, decrease size to original
frogger.addEventListener('mouseout', () => {
  frogger.style.height = "70px";
  frogger.style.width = "70px";
});

//click space to reset game
const gameBoard = document.querySelector("#board");

gameBoard.addEventListener("keypress", () => {
  gameBoard.classList.add("board");
  console.log("Key Pressed!");
});
