package main

import (
	"fmt"
	"os/exec"
)

func main() {
	// curl コマンドを使う例
	out, err := exec.Command("curl", "-s", "https://example.com").Output()
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))

	// wget コマンドを使う例
	exec.Command("wget", "https://example.com", "-O", "output.html").Run()
}
