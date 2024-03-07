const itemData = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]

describe('Saucedemo Happy Path', () => {
  beforeEach(() => {
    cy.visit('https://www.saucedemo.com/')

    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()

    cy.url().should('include', '/inventory')
  })

  it('Buys all items from the Saucedemo store', () => {
    // User is on inventory page and can add all items to cart
    cy.get('button:contains("Add to cart")').each(($el) => {
      cy.wrap($el).click()
    })

    // Go to shopping cart and make sure 6 items are in cart
    cy.get('.shopping_cart_link').click()
    cy.url().should('include', '/cart')
    cy.get('button:contains("Remove")').should('have.length', 6)

    // User can complete checkout step 1
    cy.get('[data-test="checkout"]').click()
    cy.url().should('include', '/checkout-step-one')
    cy.get('[data-test="firstName"]').type('test')
    cy.get('[data-test="lastName"]').type('user')
    cy.get('[data-test="postalCode"]').type('55555')
    cy.get('[data-test="continue"]').click()

    // User can complete checkout step 2
    cy.url().should('include', '/checkout-step-two')
    cy.get('.cart_item_label').should('have.length', 6)
    cy.get('[data-test="finish"]').click()

    // Checkout successfully completed and user can return to main inventory page
    cy.url().should('include', '/checkout-complete')
    cy.get('.complete-header').should('have.text', 'Thank you for your order!')
    cy.get('[data-test="back-to-products"]').click()
    cy.url().should('include', '/inventory')
  })

  it('Logs the user out of the application', () => {
    cy.get('#react-burger-menu-btn').click()
    cy.get('#logout_sidebar_link').click()

    cy.url().should('equal', 'https://www.saucedemo.com/')
  })
})

function arrayEquals(a, b) {
  return Array.isArray(a) &&
      Array.isArray(b) &&
      a.length === b.length &&
      a.every((val, index) => val === b[index]);
}