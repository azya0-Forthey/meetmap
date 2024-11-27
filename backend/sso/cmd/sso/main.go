package main

import (
	"fmt"
	"sso/internal/config"
)

func main() {
	conf := config.MustLoad()

	fmt.Println(conf)
}
