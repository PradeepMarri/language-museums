"""
MCP Server - Python Implementation
"""

import os
import json
import requests
from pathlib import Path
from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("MCP Server")

def get_config():
    """Get configuration from environment or config file."""
    class Config:
        def __init__(self):
            self.base_url = os.getenv("API_BASE_URL")
            self.bearer_token = os.getenv("API_BEARER_TOKEN")
            
            # Try to load from config file if env vars not set
            if not self.base_url or not self.bearer_token:
                config_path = Path.home() / ".api" / "config.json"
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                        self.base_url = self.base_url or config_data.get("baseURL")
                        self.bearer_token = self.bearer_token or config_data.get("bearerToken")
    
    return Config()

# Add configuration resource
@mcp.resource("config://settings")
def get_config_resource() -> str:
    """Get current configuration settings."""
    config = get_config()
    return json.dumps({
        "base_url": config.base_url,
        "bearer_token": "***" if config.bearer_token else None
    }, indent=2)

# Tool functions
@mcp.tool()
def get_word_json_word_top_example(word: Annotated[str, Field(description="Word to fetch examples for")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")]) -> str:
    """Returns a top example for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_etymologies(word: Annotated[str, Field(description="Word to return")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")]) -> str:
    """Fetches etymology data"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_scrabble_score(word: Annotated[str, Field(description="Word to get scrabble score for.")]) -> str:
    """Returns the Scrabble score for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_pronunciations(word: Annotated[str, Field(description="Word to get pronunciations for")], useCanonical: Annotated[str, Field(description="If true will try to return a correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], sourceDictionary: Annotated[str, Field(description="Get from a single dictionary")], typeFormat: Annotated[str, Field(description="Text pronunciation type")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Returns text pronunciations for a given word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if sourceDictionary: params["sourceDictionary"] = sourceDictionary
        if typeFormat: params["typeFormat"] = typeFormat
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_definitions(word: Annotated[str, Field(description="Word to return definitions for")], partOfSpeech: Annotated[str, Field(description="CSV list of part-of-speech types")], includeRelated: Annotated[str, Field(description="Return related words with definitions")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], includeTags: Annotated[str, Field(description="Return a closed set of XML tags in response")], limit: Annotated[str, Field(description="Maximum number of results to return")], sourceDictionaries: Annotated[str, Field(description="Source dictionary to return definitions from. If \'all\' is received, results are returned from all sources. If multiple values are received (e.g. \'century,wiktionary\'), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet")]) -> str:
    """Return definitions for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if partOfSpeech: params["partOfSpeech"] = partOfSpeech
        if includeRelated: params["includeRelated"] = includeRelated
        if useCanonical: params["useCanonical"] = useCanonical
        if includeTags: params["includeTags"] = includeTags
        if limit: params["limit"] = limit
        if sourceDictionaries: params["sourceDictionaries"] = sourceDictionaries
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_hyphenation(word: Annotated[str, Field(description="Word to get syllables for")], useCanonical: Annotated[str, Field(description="If true will try to return a correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], sourceDictionary: Annotated[str, Field(description="Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet.")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Returns syllable information for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if sourceDictionary: params["sourceDictionary"] = sourceDictionary
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_related_words(word: Annotated[str, Field(description="Word to fetch relationships for")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], relationshipTypes: Annotated[str, Field(description="Limits the total results per type of relationship type")], limitPerRelationshipType: Annotated[str, Field(description="Restrict to the supplied relationship types")]) -> str:
    """Given a word as a string, returns relationships from the Word Graph"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if relationshipTypes: params["relationshipTypes"] = relationshipTypes
        if limitPerRelationshipType: params["limitPerRelationshipType"] = limitPerRelationshipType
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_audio(word: Annotated[str, Field(description="Word to get audio for.")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Fetches audio metadata for a word."""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_frequency(word: Annotated[str, Field(description="Word to return")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], startYear: Annotated[str, Field(description="Starting Year")], endYear: Annotated[str, Field(description="Ending Year")]) -> str:
    """Returns word usage over time"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if startYear: params["startYear"] = startYear
        if endYear: params["endYear"] = endYear
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_phrases(word: Annotated[str, Field(description="Word to fetch phrases for")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], limit: Annotated[str, Field(description="Maximum number of results to return")], wlmi: Annotated[str, Field(description="Minimum WLMI for the phrase")]) -> str:
    """Fetches bi-gram phrases for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if useCanonical: params["useCanonical"] = useCanonical
        if limit: params["limit"] = limit
        if wlmi: params["wlmi"] = wlmi
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_word_json_word_examples(word: Annotated[str, Field(description="Word to return examples for")], includeDuplicates: Annotated[str, Field(description="Show duplicate examples from different sources")], useCanonical: Annotated[str, Field(description="If true will try to return the correct word root (\'cats\' -> \'cat\'). If false returns exactly what was requested.")], skip: Annotated[str, Field(description="Results to skip")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Returns examples for a word"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if word: params["word"] = word
        if includeDuplicates: params["includeDuplicates"] = includeDuplicates
        if useCanonical: params["useCanonical"] = useCanonical
        if skip: params["skip"] = skip
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_words_json_search_query(allowRegex: Annotated[str, Field(description="Search term is a Regular Expression")], query: Annotated[str, Field(description="Search query")], caseSensitive: Annotated[str, Field(description="Search case sensitive")], includePartOfSpeech: Annotated[str, Field(description="Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], excludePartOfSpeech: Annotated[str, Field(description="Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], minCorpusCount: Annotated[str, Field(description="Minimum corpus frequency for terms")], maxCorpusCount: Annotated[str, Field(description="Maximum corpus frequency for terms")], minDictionaryCount: Annotated[str, Field(description="Minimum number of dictionary entries for words returned")], maxDictionaryCount: Annotated[str, Field(description="Maximum dictionary definition count")], minLength: Annotated[str, Field(description="Minimum word length")], maxLength: Annotated[str, Field(description="Maximum word length")], skip: Annotated[str, Field(description="Results to skip")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Searches words"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if allowRegex: params["allowRegex"] = allowRegex
        if query: params["query"] = query
        if caseSensitive: params["caseSensitive"] = caseSensitive
        if includePartOfSpeech: params["includePartOfSpeech"] = includePartOfSpeech
        if excludePartOfSpeech: params["excludePartOfSpeech"] = excludePartOfSpeech
        if minCorpusCount: params["minCorpusCount"] = minCorpusCount
        if maxCorpusCount: params["maxCorpusCount"] = maxCorpusCount
        if minDictionaryCount: params["minDictionaryCount"] = minDictionaryCount
        if maxDictionaryCount: params["maxDictionaryCount"] = maxDictionaryCount
        if minLength: params["minLength"] = minLength
        if maxLength: params["maxLength"] = maxLength
        if skip: params["skip"] = skip
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_words_json_reverse_dictionary(query: Annotated[str, Field(description="Search term")], findSenseForWord: Annotated[str, Field(description="Restricts words and finds closest sense")], includeSourceDictionaries: Annotated[str, Field(description="Only include these comma-delimited source dictionaries")], excludeSourceDictionaries: Annotated[str, Field(description="Exclude these comma-delimited source dictionaries")], includePartOfSpeech: Annotated[str, Field(description="Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], excludePartOfSpeech: Annotated[str, Field(description="Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], expandTerms: Annotated[str, Field(description="Expand terms")], includeTags: Annotated[str, Field(description="Return a closed set of XML tags in response")], sortBy: Annotated[str, Field(description="Attribute to sort by")], sortOrder: Annotated[str, Field(description="Sort direction")], skip: Annotated[str, Field(description="Results to skip")], minCorpusCount: Annotated[str, Field(description="Minimum corpus frequency for terms")], maxCorpusCount: Annotated[str, Field(description="Maximum corpus frequency for terms")], minLength: Annotated[str, Field(description="Minimum word length")], maxLength: Annotated[str, Field(description="Maximum word length")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Reverse dictionary search"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if query: params["query"] = query
        if findSenseForWord: params["findSenseForWord"] = findSenseForWord
        if includeSourceDictionaries: params["includeSourceDictionaries"] = includeSourceDictionaries
        if excludeSourceDictionaries: params["excludeSourceDictionaries"] = excludeSourceDictionaries
        if includePartOfSpeech: params["includePartOfSpeech"] = includePartOfSpeech
        if excludePartOfSpeech: params["excludePartOfSpeech"] = excludePartOfSpeech
        if expandTerms: params["expandTerms"] = expandTerms
        if includeTags: params["includeTags"] = includeTags
        if sortBy: params["sortBy"] = sortBy
        if sortOrder: params["sortOrder"] = sortOrder
        if skip: params["skip"] = skip
        if minCorpusCount: params["minCorpusCount"] = minCorpusCount
        if maxCorpusCount: params["maxCorpusCount"] = maxCorpusCount
        if minLength: params["minLength"] = minLength
        if maxLength: params["maxLength"] = maxLength
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_words_json_word_of_the_day(date: Annotated[str, Field(description="Fetches by date in yyyy-MM-dd")]) -> str:
    """Returns a specific WordOfTheDay"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if date: params["date"] = date
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_words_json_random_words(hasDictionaryDef: Annotated[str, Field(description="Only return words with dictionary definitions")], includePartOfSpeech: Annotated[str, Field(description="CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], excludePartOfSpeech: Annotated[str, Field(description="CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], sortBy: Annotated[str, Field(description="Attribute to sort by")], sortOrder: Annotated[str, Field(description="Sort direction")], minCorpusCount: Annotated[str, Field(description="Minimum corpus frequency for terms")], maxCorpusCount: Annotated[str, Field(description="Maximum corpus frequency for terms")], minDictionaryCount: Annotated[str, Field(description="Minimum dictionary count")], maxDictionaryCount: Annotated[str, Field(description="Maximum dictionary count")], minLength: Annotated[str, Field(description="Minimum word length")], maxLength: Annotated[str, Field(description="Maximum word length")], limit: Annotated[str, Field(description="Maximum number of results to return")]) -> str:
    """Returns an array of random WordObjects"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if hasDictionaryDef: params["hasDictionaryDef"] = hasDictionaryDef
        if includePartOfSpeech: params["includePartOfSpeech"] = includePartOfSpeech
        if excludePartOfSpeech: params["excludePartOfSpeech"] = excludePartOfSpeech
        if sortBy: params["sortBy"] = sortBy
        if sortOrder: params["sortOrder"] = sortOrder
        if minCorpusCount: params["minCorpusCount"] = minCorpusCount
        if maxCorpusCount: params["maxCorpusCount"] = maxCorpusCount
        if minDictionaryCount: params["minDictionaryCount"] = minDictionaryCount
        if maxDictionaryCount: params["maxDictionaryCount"] = maxDictionaryCount
        if minLength: params["minLength"] = minLength
        if maxLength: params["maxLength"] = maxLength
        if limit: params["limit"] = limit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_words_json_random_word(hasDictionaryDef: Annotated[str, Field(description="Only return words with dictionary definitions")], includePartOfSpeech: Annotated[str, Field(description="CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], excludePartOfSpeech: Annotated[str, Field(description="CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)")], minCorpusCount: Annotated[str, Field(description="Minimum corpus frequency for terms")], maxCorpusCount: Annotated[str, Field(description="Maximum corpus frequency for terms")], minDictionaryCount: Annotated[str, Field(description="Minimum dictionary count")], maxDictionaryCount: Annotated[str, Field(description="Maximum dictionary count")], minLength: Annotated[str, Field(description="Minimum word length")], maxLength: Annotated[str, Field(description="Maximum word length")]) -> str:
    """Returns a single random WordObject"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if hasDictionaryDef: params["hasDictionaryDef"] = hasDictionaryDef
        if includePartOfSpeech: params["includePartOfSpeech"] = includePartOfSpeech
        if excludePartOfSpeech: params["excludePartOfSpeech"] = excludePartOfSpeech
        if minCorpusCount: params["minCorpusCount"] = minCorpusCount
        if maxCorpusCount: params["maxCorpusCount"] = maxCorpusCount
        if minDictionaryCount: params["minDictionaryCount"] = minDictionaryCount
        if maxDictionaryCount: params["maxDictionaryCount"] = maxDictionaryCount
        if minLength: params["minLength"] = minLength
        if maxLength: params["maxLength"] = maxLength
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    mcp.run()
