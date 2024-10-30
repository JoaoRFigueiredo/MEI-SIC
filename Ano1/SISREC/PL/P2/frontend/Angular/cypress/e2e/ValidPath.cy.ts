describe('cypress.config.ts', () => {
  it('should have the correct baseUrl', () => {
  

    cy.get('https://eletricgolapr5.azurewebsites.net/get-paths')
      .should('have.value', 'https://eletricgolapr5.azurewebsites.net/get-paths');
  });

  it('should have the correct defaultCommandTimeout', () => {
   

    cy.get('warehouse of departure')
      .should('have.value', '15');
  });
});
