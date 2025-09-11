package main

import (
	"cheetah/internal/database"
	"cheetah/internal/handlers"
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	InitializeDatabase()
	StartAPI()
}

func StartAPI() {
	r := gin.Default()
	
	r.GET("/ping", handlers.Ping)
	r.POST("/activity_type", handlers.CreateActivity)
	r.POST("/record", handlers.CreateRecord)
	r.PATCH("/record/:id", handlers.ApproveRecord)

	log.Println("Server starting on :8080")
	r.Run()
}

func InitializeDatabase() {
	if err := database.Initialize(); err != nil {
		log.Fatalf("Failed to initialize database: %v", err)
	}
}
