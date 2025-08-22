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

func GetaudioHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		wordVal, ok := args["word"]
		if !ok {
			return mcp.NewToolResultError("Missing required path parameter: word"), nil
		}
		word, ok := wordVal.(string)
		if !ok {
			return mcp.NewToolResultError("Invalid path parameter: word"), nil
		}
		queryParams := make([]string, 0)
		if val, ok := args["useCanonical"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("useCanonical=%v", val))
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
		url := fmt.Sprintf("%s/word.json/%s/audio%s", cfg.BaseURL, word, queryString)
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
		var result []AudioFile
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

func CreateGetaudioTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("get_word_json_word_audio",
		mcp.WithDescription("Fetches audio metadata for a word."),
		mcp.WithString("word", mcp.Required(), mcp.Description("Word to get audio for.")),
		mcp.WithString("useCanonical", mcp.Description("If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.")),
		mcp.WithNumber("limit", mcp.Description("Maximum number of results to return")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    GetaudioHandler(cfg),
	}
}
