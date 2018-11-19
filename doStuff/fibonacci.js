const fibonacciRecursion = n =>
    n <= 1 ? n :  fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

module.exports = {
  fibonacci(n) {
    const sequence = []
    for (let i = 0; i< n; i++) {
        sequence.push(fibonacciRecursion(i))
    }
    return sequence    
  }
}

