const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: '8tofka',
  e2e: {
    chromeWebSecurity: false,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
