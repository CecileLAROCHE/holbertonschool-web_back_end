import Currency from './3-currency.js';

export default class Pricing {
constructor(amount, currency){
this._amount = amount;
this._currency = currency;

// ----- getters et setters -----
  
  // amount
  get amount() {
    // retourne l'attribut _amount
  }

  set amount(value) {
    // optionnel : vérifier que c'est un nombre
    // puis assigner à _amount
  }

  // currency
  get currency() {
    // retourne l'attribut _currency
  }

  set currency(value) {
    // optionnel : vérifier que c'est une instance de Currency
    // puis assigner à _currency
  }

  // ----- méthode d'instance -----
  displayFullPrice() {
    // doit retourner : amount currency_name (currency_code)
    // exemple : 100 Euro (EUR)
  }

  // ----- méthode statique -----
  static convertPrice(amount, conversionRate) {
    // retourne amount * conversionRate
  }
}
}
}