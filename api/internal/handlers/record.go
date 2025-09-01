package handlers

import (
	"cheetah/internal/database"
	"cheetah/internal/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CreateRecord(c *gin.Context) {
	var record models.Record

	c.ShouldBindJSON(&record)

	db := database.GetDB()

	db.Create(&record)

	c.JSON(http.StatusCreated, gin.H{
		"message": "Record submission created successfully",
		"record":  record,
	})
}

func ApproveRecord(c *gin.Context, recordID string) {
	var record models.Record
	db := database.GetDB()

	db.First(&record, recordID)
	record.IsApproved = true
	db.Save(&record)

	c.JSON(http.StatusOK, gin.H{
		"message": "Record approved successfully",
		"record":  record,
	})
}
