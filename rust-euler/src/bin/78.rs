use cached::proc_macro::cached;

fn main() {
    let mut value = 0;
    let target_factor = 1_000_000;

    loop {
        let partitions = num_partitions(value, Some(target_factor));
        if partitions % target_factor == 0 {
            println!("{value} has a number of partitions divisible by {target_factor}");

            return;
        }

        value += 1;
    }
}

#[cached]
fn num_partitions(size: isize, maybe_modulo: Option<isize>) -> isize {
    // derived from https://math.stackexchange.com/questions/2675382/calculating-integer-partitions
    if size == 0 {
        return 1;
    }

    (1..=size)
        .map(|k| {
            let coefficient = if k % 2 == 1 { 1 } else { -1 };

            [pentagonal_number(k), pentagonal_number(-k)]
                .iter()
                .filter_map(|&t| {
                    if size >= t {
                        let piece = coefficient * num_partitions(size - t, maybe_modulo);

                        if let Some(modulo) = maybe_modulo {
                            Some(piece % modulo)
                        } else {
                            Some(piece)
                        }
                    } else {
                        None
                    }
                })
                .sum::<isize>()
        })
        .sum()
}

fn pentagonal_number(n: isize) -> isize {
    (n * (3 * n - 1)) / 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        assert_eq!(num_partitions(5), 7)
    }
}
