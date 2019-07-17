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

console.log("script is running...")

const myAlarm = (wakeUpTime) =>{
  return "Hey, JET, wake up! It's " + wakeUpTime;

};

const momAlarm = (wakeUpTime) =>{
  return "Hey, MOM, wake up! It's " + wakeUpTime;

};

const familyAlarm = (wakeUpTime, wakeUpPerson) =>{
  return "Hey, " + wakeUpPerson + " wake up! It's " + wakeUpTime;

};

const importantAlarm = (inputMessage) =>{
  return inputMessage.toUpperCase();

};

const snoozeAlarm = (numberTime) =>{
  return "The alarm for " + numberTime + " has been changed to " + ++numberTime;
};

const specialAlarm = (numOfPeople) =>{
let reMessage = "Wake up!"";
return reMessage.repeat(numOfPeople);

}
