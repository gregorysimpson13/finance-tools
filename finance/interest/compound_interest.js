// this example assumes that interest is compounded yearly
function compoundInterestYearly(principal = 100, interest = 0.07, years = 3) {
  return principal * Math.pow(1 + interest, years);
}

// this example assumes that interest is compounded yearly
function simpledInterestYearly(principal = 100, interest = 0.07, years = 3) {
  return principal * (1 + interest * years);
}

function doubleMoneyComplex(interest = 0.72) {
  // doubledMoney = principal * (interest + 1) ^ years
  // 2 = (interest + 1) ^ years
  return Math.log10(2) / Math.log10(1 + interest);
}

// The rule of 72
function doubleMoneySimple(interest = 0.72) {
  return 72 / (interest * 100);
}

// advertized rate
function dailyRateToAPR(dailyRate) {
  return dailyRate * 365;
}

// mathmatically correct APR
function effectiveAPR(dailyRate) {
  return 100 * (Math.pow(dailyRate + 1, 365) - 1);
}

// payday loans - want to see pay stub, pay date, bank statements
// eg. for every $100 borrowed pay an extra $25 for two weeks
function paydayLoansAPR(interestRate, time) {
  return interestRate * (52 / time) * 100;
}

// e and compound interest
function compound(principal, interestRate, periods, times) {
  return principal * Math.pow(1 + interestRate / periods, periods * times);
}

// e and compound interest
function continuousCompound(principal, interestRate, times) {
  return principal * Math.exp(interestRate * times);
}

//console.log(compoundInterestYearly(100, 0.1, 10));
//console.log(doubleMoneyComplex(0.06));
//console.log(doubleMoneySimple(0.06));
