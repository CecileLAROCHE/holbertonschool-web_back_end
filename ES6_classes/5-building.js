export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Vérifie si la méthode evacuationWarningMessage a été redéfinie
    if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error("Class extending Building must override evacuationWarningMessage");
    }
  }

  // ----- getter -----
  get sqft() {
    return this._sqft;
  }

  // ----- méthode abstraite -----
  evacuationWarningMessage() {
    // Méthode vide dans le parent
    // Toute classe enfant doit la redéfinir
  }
}
