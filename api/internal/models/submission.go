package models

import (
	"time"

	"gorm.io/gorm"
)

type Submission struct {
	gorm.Model
	DiscordID    string    `json:"discord_id"`
	Party        []string  `json:"party"`
	ActivityID   string    `json:"activity_id"`
	PersonalBest time.Time `json:"personal_best"`
	Approved     bool      `json:"approved"`
	ImgurUrl     string    `json:"imgur_url"`
}