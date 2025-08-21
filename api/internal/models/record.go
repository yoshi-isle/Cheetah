package models

import "gorm.io/gorm"

type Record struct {
	gorm.Model
	ActivityID    string    `json:"activity_id"`
	IsApproved    bool      `json:"is_approved"`
	Members       string    `json:"members"`
	PersonalBest  int       `json:"personal_best"`
	SubmissionUrl string    `json:"submission_url"`
}

