package database

import (
	"cheetah/internal/config"
	"cheetah/internal/models"
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

var db *gorm.DB

func Initialize() error {
	dsn := config.GetDatabaseURL()

	config := &gorm.Config{
		Logger: logger.Default.LogMode(logger.Info),
	}

	var err error
	db, err = gorm.Open(postgres.Open(dsn), config)
	if err != nil {
		return fmt.Errorf("failed to connect to database: %w", err)
	}

	Migrate(
		models.Activity{},
		models.Submission{},
	)

	fmt.Println("✅ Database connected successfully!")
	return nil
}

func GetDB() *gorm.DB {
	if db == nil {
		panic("Database not initialized. Call Initialize() first.")
	}
	return db
}

func Migrate(models ...interface{}) error {
	fmt.Printf("Running database migration on %v...\n", models)
	if db == nil {
		return fmt.Errorf("database not initialized")
	}

	return db.AutoMigrate(models...)
}
