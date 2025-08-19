package models

import "gorm.io/gorm"

type Activity struct {
	gorm.Model
	Name           string       `json:"name"`
	IsTimeBased    bool         `json:"is_time_based"`
}