describe('Counter', () => {
    beforeEach(() => {
      cy.visit('http://localhost:4200');
    });
  
    it('has the correct title', () => {
      console.log(cy.title());
      cy.title().should('equal', 'EletricGo');
    });
  });
  describe('GetTrucks', () => {
    it('should display a list of trucks', () => {
      cy.visit('http://localhost:4200/get-trucks');
      cy.get('table').should('contain', 'Plate');
      cy.get('table tbody tr').should('have.length.greaterThan', 0);
    });
  });
  
  