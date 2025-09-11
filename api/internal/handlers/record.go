package handlers

import (
	"cheetah/internal/database"
	"cheetah/internal/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CreateRecord(c *gin.Context) {
	var record models.Record
	var activity models.Activity

	c.ShouldBindJSON(&record)

	db := database.GetDB()
	
	if err := db.First(&activity, record.ActivityID).Error; err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Activity with this ID does not exist"})
		return
	}

	db.Create(&record)

	c.JSON(http.StatusCreated, gin.H{
		"message": "Record submission created successfully",
		"record":  record,
	})
}

func ApproveRecord(c *gin.Context) {
	var record models.Record
	db := database.GetDB()
	recordID := c.Param("id")

	if err := db.First(&record, recordID).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Record not found"})
		return
	}

	record.IsApproved = true
	if err := db.Save(&record).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to approve record"})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"message": "Record approved successfully",
		"record":  record,
	})
}
