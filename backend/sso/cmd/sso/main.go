package main

import (
	"log/slog"
	"os"
	"sso/internal/config"
)

func main() {
	conf := config.MustLoad()

	log := setupLogger(conf.Env)

	log.Info("starting application",
		slog.String("env", conf.Env),
		slog.Any("config", conf),
		slog.Int("port", conf.GRPConfig.Port),
	)
}

func setupLogger(env string) *slog.Logger {
	var log *slog.Logger

	switch env {
	case "prod":
		log = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo}))
	case "local":
		log = slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	}

	return log
}
