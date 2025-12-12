const cloneSymbol = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Crée un nouvel objet de la même classe que this
    const NewCar = this.constructor;

    // Utilise le Symbol pour éviter de copier les attributs
    return new NewCar();
  }
}
