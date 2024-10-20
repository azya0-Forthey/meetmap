package main

import (
	"api/source/config"
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

func main() {
	conf := config.GetConfig()

	db, err := sql.Open("postgres", conf.SQL_URL())
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(conf.SQL_URL())

	defer db.Close()
}
