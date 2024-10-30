describe('Counter', () => {
  beforeEach(() => {
    cy.visit('http://localhost:4200');
  });

  it('has the correct title', () => {
    console.log(cy.title());
    cy.title().should('equal', 'EletricGo');
  });
});
describe('GetPaths', () => {
  it('should display a list of paths', () => {
    cy.visit('http://localhost:4200/get-paths');
    cy.get('table').should('contain', 'Distance');
    cy.get('table tbody tr').should('have.length.greaterThan', 0);
  });
});

