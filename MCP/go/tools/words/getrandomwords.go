package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"

	"github.com/wordnik/mcp-server/config"
	"github.com/wordnik/mcp-server/models"
	"github.com/mark3labs/mcp-go/mcp"
)

func GetrandomwordsHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		queryParams := make([]string, 0)
		if val, ok := args["hasDictionaryDef"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("hasDictionaryDef=%v", val))
		}
		if val, ok := args["includePartOfSpeech"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("includePartOfSpeech=%v", val))
		}
		if val, ok := args["excludePartOfSpeech"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("excludePartOfSpeech=%v", val))
		}
		if val, ok := args["minCorpusCount"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("minCorpusCount=%v", val))
		}
		if val, ok := args["maxCorpusCount"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("maxCorpusCount=%v", val))
		}
		if val, ok := args["minDictionaryCount"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("minDictionaryCount=%v", val))
		}
		if val, ok := args["maxDictionaryCount"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("maxDictionaryCount=%v", val))
		}
		if val, ok := args["minLength"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("minLength=%v", val))
		}
		if val, ok := args["maxLength"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("maxLength=%v", val))
		}
		if val, ok := args["sortBy"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("sortBy=%v", val))
		}
		if val, ok := args["sortOrder"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("sortOrder=%v", val))
		}
		if val, ok := args["limit"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("limit=%v", val))
		}
		// Fallback to single auth parameter
		if cfg.APIKey != "" {
			queryParams = append(queryParams, fmt.Sprintf("api_key=%s", cfg.APIKey))
		}
		queryString := ""
		if len(queryParams) > 0 {
			queryString = "?" + strings.Join(queryParams, "&")
		}
		url := fmt.Sprintf("%s/words.json/randomWords%s", cfg.BaseURL, queryString)
		req, err := http.NewRequest("GET", url, nil)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to create request", err), nil
		}
		// Set authentication based on auth type
		// Fallback to single auth parameter
		if cfg.APIKey != "" {
			// API key already added to query string
		}
		req.Header.Set("Accept", "application/json")

		resp, err := http.DefaultClient.Do(req)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Request failed", err), nil
		}
		defer resp.Body.Close()

		body, err := io.ReadAll(resp.Body)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to read response body", err), nil
		}

		if resp.StatusCode >= 400 {
			return mcp.NewToolResultError(fmt.Sprintf("API error: %s", body)), nil
		}
		// Use properly typed response
		var result []WordObject
		if err := json.Unmarshal(body, &result); err != nil {
			// Fallback to raw text if unmarshaling fails
			return mcp.NewToolResultText(string(body)), nil
		}

		prettyJSON, err := json.MarshalIndent(result, "", "  ")
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to format JSON", err), nil
		}

		return mcp.NewToolResultText(string(prettyJSON)), nil
	}
}

func CreateGetrandomwordsTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("get_words_json_randomWords",
		mcp.WithDescription("Returns an array of random WordObjects"),
		mcp.WithString("hasDictionaryDef", mcp.Description("Only return words with dictionary definitions")),
		mcp.WithString("includePartOfSpeech", mcp.Description("CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")),
		mcp.WithString("excludePartOfSpeech", mcp.Description("CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")),
		mcp.WithNumber("minCorpusCount", mcp.Description("Minimum corpus frequency for terms")),
		mcp.WithNumber("maxCorpusCount", mcp.Description("Maximum corpus frequency for terms")),
		mcp.WithNumber("minDictionaryCount", mcp.Description("Minimum dictionary count")),
		mcp.WithNumber("maxDictionaryCount", mcp.Description("Maximum dictionary count")),
		mcp.WithNumber("minLength", mcp.Description("Minimum word length")),
		mcp.WithNumber("maxLength", mcp.Description("Maximum word length")),
		mcp.WithString("sortBy", mcp.Description("Attribute to sort by")),
		mcp.WithString("sortOrder", mcp.Description("Sort direction")),
		mcp.WithNumber("limit", mcp.Description("Maximum number of results to return")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    GetrandomwordsHandler(cfg),
	}
}
