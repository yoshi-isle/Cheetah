package config

import (
	"os"
)

func GetDatabaseURL() string {
	return os.Getenv("DB_CONNECTION_STRING")
}
