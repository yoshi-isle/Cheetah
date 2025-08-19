package handlers

import (
	"cheetah/internal/database"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Ping(c *gin.Context) {
	db := database.GetDB()
	c.JSON(http.StatusOK, gin.H{
		"message": "pong",
		"database": "connected",
		"db_name": db.Name(),
	})
}