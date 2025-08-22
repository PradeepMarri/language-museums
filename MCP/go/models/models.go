package models

import (
	"context"
	"github.com/mark3labs/mcp-go/mcp"
)

type Tool struct {
	Definition mcp.Tool
	Handler    func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error)
}

// Citation represents the Citation schema from the OpenAPI specification
type Citation struct {
	Cite string `json:"cite,omitempty"`
	Source string `json:"source,omitempty"`
}

// Label represents the Label schema from the OpenAPI specification
type Label struct {
	TypeField string `json:"type,omitempty"`
	Text string `json:"text,omitempty"`
}

// Definition represents the Definition schema from the OpenAPI specification
type Definition struct {
	Exampleuses []interface{} `json:"exampleUses,omitempty"`
	Extendedtext string `json:"extendedText,omitempty"`
	Sequence string `json:"sequence,omitempty"`
	Textprons []interface{} `json:"textProns,omitempty"`
	Notes []interface{} `json:"notes,omitempty"`
	Attributionurl string `json:"attributionUrl,omitempty"`
	Text string `json:"text,omitempty"`
	Seqstring string `json:"seqString,omitempty"`
	Attributiontext string `json:"attributionText,omitempty"`
	Relatedwords []interface{} `json:"relatedWords,omitempty"`
	Citations []interface{} `json:"citations,omitempty"`
	Word string `json:"word,omitempty"`
	Score float32 `json:"score,omitempty"`
	Sourcedictionary string `json:"sourceDictionary,omitempty"`
	Labels []interface{} `json:"labels,omitempty"`
	Partofspeech string `json:"partOfSpeech,omitempty"`
}

// ExampleUsage represents the ExampleUsage schema from the OpenAPI specification
type ExampleUsage struct {
	Text string `json:"text,omitempty"`
}

// Example represents the Example schema from the OpenAPI specification
type Example struct {
	Id int64 `json:"id,omitempty"`
	Rating float32 `json:"rating,omitempty"`
	Text string `json:"text,omitempty"`
	Year int `json:"year,omitempty"`
	Url string `json:"url,omitempty"`
	Word string `json:"word,omitempty"`
	Exampleid int64 `json:"exampleId,omitempty"`
	Sentence Sentence `json:"sentence,omitempty"`
	Documentid int64 `json:"documentId,omitempty"`
	Provider ContentProvider `json:"provider,omitempty"`
	Score ScoredWord `json:"score,omitempty"`
	Title string `json:"title,omitempty"`
}

// Note represents the Note schema from the OpenAPI specification
type Note struct {
	Notetype string `json:"noteType,omitempty"`
	Pos int `json:"pos,omitempty"`
	Value string `json:"value,omitempty"`
	Appliesto []string `json:"appliesTo,omitempty"`
}

// AudioFile represents the AudioFile schema from the OpenAPI specification
type AudioFile struct {
	Commentcount int `json:"commentCount,omitempty"`
	Createdat string `json:"createdAt,omitempty"`
	Createdby string `json:"createdBy,omitempty"`
	Fileurl string `json:"fileUrl,omitempty"`
	Id int64 `json:"id"`
	Votecount int `json:"voteCount,omitempty"`
	Attributiontext string `json:"attributionText,omitempty"`
	Description string `json:"description,omitempty"`
	Voteweightedaverage float32 `json:"voteWeightedAverage,omitempty"`
	Duration float64 `json:"duration,omitempty"`
	Audiotype string `json:"audioType,omitempty"`
	Voteaverage float32 `json:"voteAverage,omitempty"`
	Word string `json:"word,omitempty"`
	Attributionurl string `json:"attributionUrl,omitempty"`
}

// FacetValue represents the FacetValue schema from the OpenAPI specification
type FacetValue struct {
	Value string `json:"value,omitempty"`
	Count int64 `json:"count,omitempty"`
}

// WordOfTheDay represents the WordOfTheDay schema from the OpenAPI specification
type WordOfTheDay struct {
	Publishdate string `json:"publishDate,omitempty"`
	Contentprovider ContentProvider `json:"contentProvider,omitempty"`
	Examples []interface{} `json:"examples,omitempty"`
	Id int64 `json:"id"`
	Createdby string `json:"createdBy,omitempty"`
	Htmlextra string `json:"htmlExtra,omitempty"`
	Note string `json:"note,omitempty"`
	Word string `json:"word,omitempty"`
	Definitions []interface{} `json:"definitions,omitempty"`
	Category string `json:"category,omitempty"`
	Createdat string `json:"createdAt,omitempty"`
	Parentid string `json:"parentId,omitempty"`
}

// SimpleDefinition represents the SimpleDefinition schema from the OpenAPI specification
type SimpleDefinition struct {
	Partofspeech string `json:"partOfSpeech,omitempty"`
	Source string `json:"source,omitempty"`
	Text string `json:"text,omitempty"`
	Note string `json:"note,omitempty"`
}

// Sentence represents the Sentence schema from the OpenAPI specification
type Sentence struct {
	Scoredwords []interface{} `json:"scoredWords,omitempty"`
	Display string `json:"display,omitempty"`
	Documentmetadataid int64 `json:"documentMetadataId,omitempty"`
	Hasscoredwords bool `json:"hasScoredWords,omitempty"`
	Id int64 `json:"id,omitempty"`
	Rating int `json:"rating,omitempty"`
}

// WordListWord represents the WordListWord schema from the OpenAPI specification
type WordListWord struct {
	Username string `json:"username,omitempty"`
	Word string `json:"word,omitempty"`
	Createdat string `json:"createdAt,omitempty"`
	Id int64 `json:"id"`
	Numbercommentsonword int64 `json:"numberCommentsOnWord,omitempty"`
	Numberlists int64 `json:"numberLists,omitempty"`
	Userid int64 `json:"userId,omitempty"`
}

// ContentProvider represents the ContentProvider schema from the OpenAPI specification
type ContentProvider struct {
	Id int `json:"id,omitempty"`
	Name string `json:"name,omitempty"`
}

// ScoredWord represents the ScoredWord schema from the OpenAPI specification
type ScoredWord struct {
	Lemma string `json:"lemma,omitempty"`
	Score float32 `json:"score,omitempty"`
	Stopword bool `json:"stopword,omitempty"`
	Wordtype string `json:"wordType,omitempty"`
	Basewordscore float64 `json:"baseWordScore,omitempty"`
	Partofspeech string `json:"partOfSpeech,omitempty"`
	Position int `json:"position,omitempty"`
	Sentenceid int64 `json:"sentenceId,omitempty"`
	Word string `json:"word,omitempty"`
	Doctermcount int `json:"docTermCount,omitempty"`
	Id int64 `json:"id,omitempty"`
}

// PartOfSpeech represents the PartOfSpeech schema from the OpenAPI specification
type PartOfSpeech struct {
	Allcategories []interface{} `json:"allCategories,omitempty"`
	Roots []interface{} `json:"roots,omitempty"`
	Storageabbr []string `json:"storageAbbr,omitempty"`
}

// DefinitionSearchResults represents the DefinitionSearchResults schema from the OpenAPI specification
type DefinitionSearchResults struct {
	Results []interface{} `json:"results,omitempty"`
	Totalresults int `json:"totalResults,omitempty"`
}

// Syllable represents the Syllable schema from the OpenAPI specification
type Syllable struct {
	Text string `json:"text,omitempty"`
	TypeField string `json:"type,omitempty"`
	Seq int `json:"seq,omitempty"`
}

// WordSearchResult represents the WordSearchResult schema from the OpenAPI specification
type WordSearchResult struct {
	Lexicality float64 `json:"lexicality,omitempty"`
	Word string `json:"word,omitempty"`
	Count int64 `json:"count,omitempty"`
}

// Frequency represents the Frequency schema from the OpenAPI specification
type Frequency struct {
	Year int `json:"year,omitempty"`
	Count int64 `json:"count,omitempty"`
}

// WordList represents the WordList schema from the OpenAPI specification
type WordList struct {
	Numberwordsinlist int64 `json:"numberWordsInList,omitempty"`
	Permalink string `json:"permalink,omitempty"`
	TypeField string `json:"type,omitempty"`
	Createdat string `json:"createdAt,omitempty"`
	Id int64 `json:"id"`
	Name string `json:"name,omitempty"`
	Userid int64 `json:"userId,omitempty"`
	Description string `json:"description,omitempty"`
	Updatedat string `json:"updatedAt,omitempty"`
	Username string `json:"username,omitempty"`
	Lastactivityat string `json:"lastActivityAt,omitempty"`
}

// SimpleExample represents the SimpleExample schema from the OpenAPI specification
type SimpleExample struct {
	Id int64 `json:"id,omitempty"`
	Text string `json:"text,omitempty"`
	Title string `json:"title,omitempty"`
	Url string `json:"url,omitempty"`
}

// Long represents the Long schema from the OpenAPI specification
type Long struct {
	Value int64 `json:"value,omitempty"`
}

// TextPron represents the TextPron schema from the OpenAPI specification
type TextPron struct {
	Raw string `json:"raw,omitempty"`
	Rawtype string `json:"rawType,omitempty"`
	Seq int `json:"seq,omitempty"`
}

// WordSearchResults represents the WordSearchResults schema from the OpenAPI specification
type WordSearchResults struct {
	Totalresults int `json:"totalResults,omitempty"`
	Searchresults []interface{} `json:"searchResults,omitempty"`
}

// Root represents the Root schema from the OpenAPI specification
type Root struct {
	Categories []interface{} `json:"categories,omitempty"`
	Id int64 `json:"id"`
	Name string `json:"name,omitempty"`
}

// WordObject represents the WordObject schema from the OpenAPI specification
type WordObject struct {
	Word string `json:"word,omitempty"`
	Canonicalform string `json:"canonicalForm,omitempty"`
	Id int64 `json:"id"`
	Originalword string `json:"originalWord,omitempty"`
	Suggestions []string `json:"suggestions,omitempty"`
	Vulgar string `json:"vulgar,omitempty"`
}

// Category represents the Category schema from the OpenAPI specification
type Category struct {
	Id int64 `json:"id"`
	Name string `json:"name,omitempty"`
}

// FrequencySummary represents the FrequencySummary schema from the OpenAPI specification
type FrequencySummary struct {
	Unknownyearcount int `json:"unknownYearCount,omitempty"`
	Word string `json:"word,omitempty"`
	Frequency []interface{} `json:"frequency,omitempty"`
	Frequencystring string `json:"frequencyString,omitempty"`
	Totalcount int64 `json:"totalCount,omitempty"`
}

// AudioType represents the AudioType schema from the OpenAPI specification
type AudioType struct {
	Id int `json:"id,omitempty"`
	Name string `json:"name,omitempty"`
}

// ApiTokenStatus represents the ApiTokenStatus schema from the OpenAPI specification
type ApiTokenStatus struct {
	Totalrequests int64 `json:"totalRequests,omitempty"`
	Valid bool `json:"valid,omitempty"`
	Expiresinmillis int64 `json:"expiresInMillis,omitempty"`
	Remainingcalls int64 `json:"remainingCalls,omitempty"`
	Resetsinmillis int64 `json:"resetsInMillis,omitempty"`
	Token string `json:"token,omitempty"`
}

// Bigram represents the Bigram schema from the OpenAPI specification
type Bigram struct {
	Count int64 `json:"count,omitempty"`
	Gram1 string `json:"gram1,omitempty"`
	Gram2 string `json:"gram2,omitempty"`
	Mi float64 `json:"mi,omitempty"`
	Wlmi float64 `json:"wlmi,omitempty"`
}

// Facet represents the Facet schema from the OpenAPI specification
type Facet struct {
	Name string `json:"name,omitempty"`
	Facetvalues []interface{} `json:"facetValues,omitempty"`
}

// StringValue represents the StringValue schema from the OpenAPI specification
type StringValue struct {
	Word string `json:"word,omitempty"`
}

// ExampleSearchResults represents the ExampleSearchResults schema from the OpenAPI specification
type ExampleSearchResults struct {
	Examples []interface{} `json:"examples,omitempty"`
	Facets []interface{} `json:"facets,omitempty"`
}

// Related represents the Related schema from the OpenAPI specification
type Related struct {
	Label2 string `json:"label2,omitempty"`
	Label3 string `json:"label3,omitempty"`
	Label4 string `json:"label4,omitempty"`
	Relationshiptype string `json:"relationshipType,omitempty"`
	Words []string `json:"words,omitempty"`
	Gram string `json:"gram,omitempty"`
	Label1 string `json:"label1,omitempty"`
}

// User represents the User schema from the OpenAPI specification
type User struct {
	Password string `json:"password,omitempty"`
	Status int `json:"status,omitempty"`
	Username string `json:"userName,omitempty"`
	Username string `json:"username,omitempty"`
	Displayname string `json:"displayName,omitempty"`
	Email string `json:"email,omitempty"`
	Facebookid string `json:"faceBookId,omitempty"`
	Id int64 `json:"id,omitempty"`
}

// AuthenticationToken represents the AuthenticationToken schema from the OpenAPI specification
type AuthenticationToken struct {
	Userid int64 `json:"userId,omitempty"`
	Usersignature string `json:"userSignature,omitempty"`
	Token string `json:"token,omitempty"`
}
