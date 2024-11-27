package config

import (
	"flag"
	"fmt"
	"github.com/ilyakaznacheev/cleanenv"
	"os"
	"time"
)

type Config struct {
	Env            string         `yaml:"env" env-required:"true"`
	TokenTTL       time.Duration  `yaml:"token_ttl" env-required:"true"`
	GRPConfig      GRPConfig      `yaml:"grpc" env-required:"true"`
	PostgresConfig PostgresConfig `yaml:"postgres" env-required:"false"`
}

type PostgresConfig struct {
	User     string `yaml:"user"`
	Name     string `yaml:"name"`
	Password string `yaml:"password"`
	Host     string `yaml:"host"`
	Port     int    `yaml:"port"`
}

type GRPConfig struct {
	Port    int           `yaml:"port"`
	Timeout time.Duration `yaml:"timeout"`
}

func MustLoad() *Config {
	path := fetchConfigPath()
	if path == "" {
		panic("config path is missed")
	}
	if _, err := os.Stat(path); os.IsNotExist(err) {
		panic(fmt.Sprintf("config path %s does not exist", path))
	}

	var config Config

	if err := cleanenv.ReadConfig(path, &config); err != nil {
		panic(fmt.Sprintf("load config file %s failed: %s", path, err))
	}

	return &config
}

func fetchConfigPath() string {
	var res string

	flag.StringVar(&res, "config", "", "config path")
	flag.Parse()

	if res == "" {
		res = os.Getenv("CONFIG_PATH")
	}

	return res
}
