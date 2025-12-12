import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Appelle du parent
    super(sqft);

    // Propriété spécifique
    this._floors = floors;
  }

  // ----- getters -----
  get floors() {
    return this._floors;
  }

  // ----- méthode override -----
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
