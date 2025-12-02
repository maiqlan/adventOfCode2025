package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func calc(r int, n string) int {
	a, b := rune(n[0]), n[1:]
	c, err := strconv.Atoi(b)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(a), c) // Process each line as needed
	if a == 'L' {
		return (r - c) % 100
	}

	return (r + c) % 100
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	r, p := 50, 0
	for scanner.Scan() {
		n := scanner.Text()
		r = calc(r, n)
		if r == 0 {
			p += 1
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading stdin:", err)
	}
	fmt.Println(p)
}
