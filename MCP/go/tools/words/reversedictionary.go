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

func ReversedictionaryHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		queryParams := make([]string, 0)
		if val, ok := args["query"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("query=%v", val))
		}
		if val, ok := args["findSenseForWord"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("findSenseForWord=%v", val))
		}
		if val, ok := args["includeSourceDictionaries"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("includeSourceDictionaries=%v", val))
		}
		if val, ok := args["excludeSourceDictionaries"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("excludeSourceDictionaries=%v", val))
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
		if val, ok := args["minLength"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("minLength=%v", val))
		}
		if val, ok := args["maxLength"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("maxLength=%v", val))
		}
		if val, ok := args["expandTerms"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("expandTerms=%v", val))
		}
		if val, ok := args["includeTags"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("includeTags=%v", val))
		}
		if val, ok := args["sortBy"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("sortBy=%v", val))
		}
		if val, ok := args["sortOrder"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("sortOrder=%v", val))
		}
		if val, ok := args["skip"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("skip=%v", val))
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
		url := fmt.Sprintf("%s/words.json/reverseDictionary%s", cfg.BaseURL, queryString)
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
		var result models.DefinitionSearchResults
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

func CreateReversedictionaryTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("get_words_json_reverseDictionary",
		mcp.WithDescription("Reverse dictionary search"),
		mcp.WithString("query", mcp.Required(), mcp.Description("Search term")),
		mcp.WithString("findSenseForWord", mcp.Description("Restricts words and finds closest sense")),
		mcp.WithString("includeSourceDictionaries", mcp.Description("Only include these comma-delimited source dictionaries")),
		mcp.WithString("excludeSourceDictionaries", mcp.Description("Exclude these comma-delimited source dictionaries")),
		mcp.WithString("includePartOfSpeech", mcp.Description("Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")),
		mcp.WithString("excludePartOfSpeech", mcp.Description("Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")),
		mcp.WithNumber("minCorpusCount", mcp.Description("Minimum corpus frequency for terms")),
		mcp.WithNumber("maxCorpusCount", mcp.Description("Maximum corpus frequency for terms")),
		mcp.WithNumber("minLength", mcp.Description("Minimum word length")),
		mcp.WithNumber("maxLength", mcp.Description("Maximum word length")),
		mcp.WithString("expandTerms", mcp.Description("Expand terms")),
		mcp.WithString("includeTags", mcp.Description("Return a closed set of XML tags in response")),
		mcp.WithString("sortBy", mcp.Description("Attribute to sort by")),
		mcp.WithString("sortOrder", mcp.Description("Sort direction")),
		mcp.WithString("skip", mcp.Description("Results to skip")),
		mcp.WithNumber("limit", mcp.Description("Maximum number of results to return")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    ReversedictionaryHandler(cfg),
	}
}
