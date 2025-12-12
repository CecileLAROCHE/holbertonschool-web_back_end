export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Vérifie si on n'est PAS dans la classe Building elle-même
    // (donc si on est dans une classe enfant)
    if (this.constructor !== Building &&
        this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error("Class extending Building must override evacuationWarningMessage");
    }
  }

  // getter
  get sqft() {
    return this._sqft;
  }

  // méthode "abstraite"
  evacuationWarningMessage() {
    // Doit être overriden par les enfants
  }
}
