uniffi_macros::include_scaffolding!("math");

// add two numbers
fn add(a: u32, b: u32) -> u32 {
    a + b
}

// return the number of prime numbers in a given range
fn num_primes_rust(lower: u32, upper: u32) -> u32 {

    let mut total: u32 = 0;

    for num in lower..(upper + 1) {
        // 0 and 1 are not prime
        if num > 1 {
            let mut prime = true;
            for i in 2..num {
                if (num % i) == 0 {
                    prime = false;
                }
            }
            if prime == true {
                total+=1
            }
        }
    }
    return total;
}
