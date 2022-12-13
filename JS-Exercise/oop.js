// class ir kā rasējums
// visas metodes un dati ir pieejami caur this. vārdiņu
class Animal {
  // # simbolizē, ka dati/metode būs privāti, un privātus datus mēs definējam ārpus konsturktora
  #minutesInYear = 525960

  // būtībā init()/onStart/firstTimeOnStart/__init__
  constructor(animalName, animalAge) {
    // pubiski dati
    this.name = animalName;
    this.age = animalAge;

    // this is klases instance, kurā ir meklējami visi dati un metodes
    // citās valodās this var saukt arī par self
    // console.log(this)
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
  sayMyAgeInMinutes() {
    console.log(`I am ${this.#calculateAgeInMinutes()} minutes old`)
  }
}

class Cat extends Animal {
  #timeOfHeightCatCanJump = 5

  constructor(animalName, animalAge, heightInCm) {
    // izsauc Animal klases konstruktoru, kas dod pieeju visam, kas ir Animal klasē
    super(animalName, animalAge)

    this.heightInCm = heightInCm
  }

  #calculateCatJump() {
    return this.heightInCm * this.#timeOfHeightCatCanJump
  }

  sayHello() {
    this.sayCatNoise()
    // super ir kā this, taču attiecas TIKAI uz Animal klasi
    super.sayHello()
    this.sayCatNoise()
  }

  sayCatNoise() {
    console.log('meow')

    this.sayMyAgeInMinutes()
  }

  howHighCanIJump() {
    console.log(`I can jump ${this.#calculateCatJump()}cm`)
  }
}

const someAnimal = new Animal('Reksis', 8)
const someCat = new Cat('Feģa', 2, 30)

console.log('### Animal Class ###')
someAnimal.sayHello()
console.log('### Cat Class ###')
someCat.sayHello()
someCat.howHighCanIJump()
someCat.sayCatNoise()