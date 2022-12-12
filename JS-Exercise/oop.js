// class ir kā rasējums
// visas metodes un dati ir pieejami caur this. vārdiņu
class Animal {
    // # simbolizē, ka dati/metode būs privāti, un privātus datus mēs definējam ārpus konsturktora
    #minutesInYear = 525960
  
    // būtībā init()/onStart/firstTimeOnStart
    constructor(animalName, animalAge) {
      // pubiski dati
      this.name = animalName;
      this.age = animalAge
    }
  
    // privāta metode
    #calculateAgeInMinutes() {
      return this.#minutesInYear * this.age
    }
  
    // publiska metode
    sayHello() {
      console.log('Hello there I am animal');
    }
  
    // publiska metode
    sayMyName() {
      console.log(`My name is ${this.name}`);
    }
  
    // publiska metode
    sayMyNameAndHello() {
      this.sayHello()
      this.sayMyName()
    }
  
    // publiska metode
    sayMyAgeInMinutes() {
      console.log(`I am ${this.#calculateAgeInMinutes()} minutes old`)
    }
  }
  
  // šī jau ir uztaisīta klases pēc rasējuma, kuru sauc arī par klases instanci
  const someAnimal = new Animal('Zheeraf', 5)