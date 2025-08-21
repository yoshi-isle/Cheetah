package handlers

import (
	"cheetah/internal/database"
	"cheetah/internal/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CreateRecord(c *gin.Context) {
	var record models.Record

	if err := c.ShouldBindJSON(&record); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON format"})
		return
	}

	db := database.GetDB()

	if err := db.Create(&record).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{
		"message": "Record submission created successfully",
		"record":  record,
	})
}