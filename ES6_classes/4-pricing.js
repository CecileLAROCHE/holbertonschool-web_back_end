import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // ----- getters et setters -----

  // amount
  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== "number") {
      throw new TypeError("Amount must be a number");
    }
    this._amount = value; 
  }

  // currency
  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError("currency must be a Currency instance");
    }
    this._currency = value; 
  }

  // ----- méthode d'instance -----
  displayFullPrice() {
    // retourne une string : amount currency_name (currency_code)
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // ----- méthode statique -----
  static convertPrice(amount, conversionRate) {
    // retourne juste amount * conversionRate
    return amount * conversionRate;
  }
}
