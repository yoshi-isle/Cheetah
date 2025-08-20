package models

type Record struct {
	ActivityID    string    `json:"activity_id"`
	IsApproved    bool      `json:"is_approved"`
	DiscordIDs    string    `json:"discord_ids"`
	PersonalBest  int       `json:"personal_best"`
	SubmissionUrl string    `json:"submission_url"`
}

