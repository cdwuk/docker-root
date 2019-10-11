package main

import (
	"fmt"
	"net/http"
	"os"
)

func getEnv(key, fallback string) string {
	value, exists := os.LookupEnv(key)
	if !exists {
		value = fallback
	}
	return value
}

func main() {
	port := getEnv("PORT", "8080")

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "This is a Go app. </ iframe height='600' width='800' src='https://www.whufc.com/' >")
	})

	http.ListenAndServe(":"+port, nil)
}
