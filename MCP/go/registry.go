package main

import (
	"github.com/wordnik/mcp-server/config"
	"github.com/wordnik/mcp-server/models"
	tools_word "github.com/wordnik/mcp-server/tools/word"
	tools_words "github.com/wordnik/mcp-server/tools/words"
)

func GetAll(cfg *config.APIConfig) []models.Tool {
	return []models.Tool{
		tools_word.CreateGetphrasesTool(cfg),
		tools_word.CreateGetscrabblescoreTool(cfg),
		tools_word.CreateGetdefinitionsTool(cfg),
		tools_word.CreateGetwordfrequencyTool(cfg),
		tools_word.CreateGetaudioTool(cfg),
		tools_words.CreateGetrandomwordsTool(cfg),
		tools_words.CreateSearchwordsTool(cfg),
		tools_word.CreateGetexamplesTool(cfg),
		tools_word.CreateGethyphenationTool(cfg),
		tools_words.CreateGetrandomwordTool(cfg),
		tools_word.CreateGetetymologiesTool(cfg),
		tools_word.CreateGetrelatedwordsTool(cfg),
		tools_words.CreateGetwordofthedayTool(cfg),
		tools_word.CreateGettextpronunciationsTool(cfg),
		tools_words.CreateReversedictionaryTool(cfg),
		tools_word.CreateGettopexampleTool(cfg),
	}
}
