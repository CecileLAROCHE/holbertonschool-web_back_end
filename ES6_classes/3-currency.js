export default class Currency {
  constructor(code, name) {
    this._code = code;   // stockage interne
    this._name = name;
  }

  // getter code
  get code() {
    return this._code;
  }

  // setter code
  set code(value) {
    this._code = value;
  }

  // getter name
  get name() {
    return this._name;
  }

  // setter name
  set name(value) {
    this._name = value;
  }

  // méthode displayFullCurrency
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
