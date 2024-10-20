package config

import (
	"fmt"
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	user     string
	password string
	name     string
	host     string
	port     string
	sslmode  bool
	debug    bool
}

func (b *Config) SQL_URL() string {
	var sslmode string

	if b.sslmode {
		sslmode = "enable"
	} else {
		sslmode = "disable"
	}

	return fmt.Sprintf(
		"user=%s password=%s dbname=%s host=%s port=%s sslmode=%s",
		b.user, b.password, b.name, b.host, b.port, sslmode,
	)
}

var config *Config = nil

func GetConfig() *Config {
	if config != nil {
		return config
	}

	var debugStr string = os.Getenv("DEBUG")
	var debug bool = debugStr == "" || debugStr == "true"

	if debug {
		err := godotenv.Load("../dev.env")

		if err != nil {
			panic("dev.env do not load")
		}
	}

	config = &Config{
		user:     os.Getenv("POSTGRES_USER"),
		password: os.Getenv("POSTGRES_PASSWORD"),
		name:     os.Getenv("POSTGRES_DB"),
		host:     os.Getenv("POSTGRES_HOST"),
		port:     os.Getenv("POSTGRES_PORT"),
		sslmode:  false,
		debug:    debug,
	}

	return config
}
