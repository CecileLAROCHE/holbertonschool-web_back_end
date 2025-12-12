export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Cast en Number → retourne size
  valueOf() {
    return this._size;
  }

  // Cast en String → retourne location
  toString() {
    return this._location;
  }
}
