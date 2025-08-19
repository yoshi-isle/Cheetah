package config

import (
	"os"

	"github.com/joho/godotenv"
)

func init() {
	err := godotenv.Load("../.env")
	if err != nil {
		panic("failed to load .env file")
	}
}

func GetDatabaseURL() string {
	return os.Getenv("DB_CONNECTION_STRING")
}
