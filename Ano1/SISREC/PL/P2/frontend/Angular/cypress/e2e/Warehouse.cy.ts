describe('GetPaths', () => {
    it('should display a list of paths', () => {
        cy.visit('http://localhost:4200/warehouses');
        cy.get('table').should('contain', 'Description');
        cy.get('table tbody tr').should('have.length.greaterThan', 0);
        cy.get('table tbody tr th a').first().should('have.text', '1');
        cy.get('table tbody tr td').first().should('have.text', 'Arouca');
    });
    it('displays different sets of warehouses based on checkbox selection', () => {
        cy.visit('http://localhost:4200/warehouses');
        let WarehousesLength;
        // Select the "All" checkbox and verify that all warehouses are displayed
        cy.get('input[name="groupA"][value="all"]').check();
        cy.get('table tbody tr').then((rows) => {
            WarehousesLength = rows.length;
          });
    
        // Select the "Enabled" checkbox and verify that only enabled warehouses are displayed
        cy.get('input[name="groupA"][value="enabled"]').check();
        cy.get('table tbody tr').should('have.length.lessThan', WarehousesLength);
    
        // Select the "Disabled" checkbox and verify that only disabled warehouses are displayed
        cy.get('input[name="groupA"][value="disabled"]').check();
        cy.get('table tbody tr').should('have.length.lessThan', WarehousesLength);
      });
});