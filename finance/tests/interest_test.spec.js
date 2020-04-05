const rewire = require("rewire");
const chai = require("chai");
const expect = chai.expect;

const app = rewire("../interest/compound_interest");
doubleMoneySimple = app.__get__("doubleMoneySimple");
simpledInterestYearly = app.__get__("simpledInterestYearly");
compoundInterestYearly = app.__get__("compoundInterestYearly");
dailyRateToAPR = app.__get__("dailyRateToAPR");
effectiveAPR = app.__get__("effectiveAPR");
paydayLoansAPR = app.__get__("paydayLoansAPR");
compound = app.__get__("compound");
continuousCompound = app.__get__("continuousCompound");

describe("compound interest", function() {
  it("estimates time it takes to double your money", function() {
    expect(doubleMoneySimple(0.72)).to.equal(1);
  });
  it("calculates the amount owed in compound interest", function() {
    expect(compoundInterestYearly(50, 0.15, 20)).to.be.closeTo(818, 1);
  });
});

describe("simple interest", function() {
  it("calculates the amount owed in simple interest", function() {
    expect(simpledInterestYearly(50, 0.15, 20)).to.equal(200);
  });
});

describe("Annual Percentage Rate", function() {
  it("Calculates the simple daily rate", function() {
    expect(dailyRateToAPR(0.06274)).to.be.closeTo(22.9, 0.1);
  });
  it("Calculates the effective interest rate", function() {
    expect(effectiveAPR(0.0006274)).to.be.closeTo(25.7, 0.1);
  });
  it("Calculates the interest rate of payday loans", function() {
    expect(paydayLoansAPR(0.25, 2)).to.equal(650);
  });
});

describe("Compound Interest Test", function() {
  it("Calculates the compound interest by period", function() {
    expect(compound(1, 1, 365, 1)).to.be.closeTo(2.71, 0.01);
    expect(compound(50, 0.1, 4, 3)).to.be.closeTo(67.24, 0.01);
  });
  it("Calculates the continuous compound interest rate", function() {
    expect(continuousCompound(50, 0.1, 3)).to.be.closeTo(67.49, 0.01);
  });
});
