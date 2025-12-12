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
    if (typeof value !== "number") throw new TypeError("Length must be a number");
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
    return ${this_amount} ${this_currency_name} (${thiscurrency_code});
  }

  // ----- méthode statique -----
  static convertPrice(amount, conversionRate) {
      return amount * conversionRate;
  }
}
