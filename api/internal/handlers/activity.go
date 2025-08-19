package handlers

import (
	"cheetah/internal/database"
	"cheetah/internal/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CreateActivity(c *gin.Context) {
	var activity models.Activity

	if err := c.ShouldBindJSON(&activity); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON format"})
		return
	}

	db := database.GetDB()

	var existingActivityType models.Activity
	if err := db.Where("name = ?", activity.Name).First(&existingActivityType).Error; err == nil {
		c.JSON(http.StatusConflict, gin.H{"error": "Activity Type with this name already exists"})
		return
	}

	if err := db.Create(&activity).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{
		"message": "ActivityType created successfully", 
		"activityType": activity,
	})
}