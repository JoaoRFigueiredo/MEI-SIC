describe('Auth', () => {
    it('should display the login form when the user is not logged in', () => {
        cy.visit('/');
        cy.get('form.login').should('be.visible');
    });

    it('should display the logout button when the user is logged in', () => {
        // log in the user
        cy.get('asl-google-signin-button#b1').click();

        cy.get('button#logOut').should('be.visible');
    });
    it('should redirect the user to the admin route when the "Admin Board" button is clicked', () => {
        // log in the user
        cy.get('asl-google-signin-button#b1').click();

        cy.get('button#b2').click();
        cy.url().should('include', '/admin');
    });
    it('should log the user in when they click the Google sign in button', () => {
        cy.visit('/');
        cy.get('asl-google-signin-button#b1').click();
        cy.get('p').contains('Your email').should('be.visible');
    });
    it('should log the user out when the "Logout" button is clicked', () => {
        // log in the user
        cy.get('asl-google-signin-button#b1').click();

        cy.get('button#logOut').click();
        cy.get('form.login').should('be.visible');
    });
});