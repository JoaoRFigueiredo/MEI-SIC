// ***********************************************************
// This example support/e2e.ts is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'

describe('Path object', () => {
    it('should have the correct warehousedeparture property', () => {
      const path = {
        warehousedeparture: 1,
        warehousedestination: 'Warehouse B',
        distance: 100
      };
  
      expect(path.warehousedeparture).to.equal(1);
    });
  });
  
// Alternatively you can use CommonJS syntax:
// require('./commands')