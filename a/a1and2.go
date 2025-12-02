package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var Globalpart = 2

func convert(n string) (rune, int) {
	a, b := rune(n[0]), n[1:]
	c, err := strconv.Atoi(b)
	if err != nil {
		panic(err)
	}
	return a, c
}

func calc1(r int, n string) int {
	a, c := convert((n))
	if a == 'L' {
		return (r - c) % 100
	}

	return (r + c) % 100
}

func calc2(r int, n string) (int, int) {
	a, b := convert((n))
	t := -1
	if a == 'L' {
		t = (r - b) % 100
	} else {
		t = (r + b) % 100
	}

	if a == 'L' && r <= b && r == 0 {
		return t, (b - r) / 100
	} else if a == 'L' && r <= b {
		return t, (b-r)/100 + 1
	} else if a == 'R' && (r+b) >= 100 {
		return t, (b + r) / 100
	}

	if t == 0 {
		return t, 1
	}

	return t, 0
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	r, p := 50, 0
	for scanner.Scan() {
		n := scanner.Text()
		if Globalpart == 1 {
			r = calc1(r, n)
			r = (r + 100) % 100
			if r == 0 {
				p += 1
			}
		} else {
			res, p0 := calc2(r, n)
			r = (res + 100) % 100
			p += p0
			fmt.Println(r, p0)
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading stdin:", err)
	}
	fmt.Println(p)
}
