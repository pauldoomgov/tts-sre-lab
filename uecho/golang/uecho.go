// Based on code from https://golang.org/doc/articles/wiki/#tmp_3

package main

import (
    "fmt"
    "log"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "<html><head><title>Unstoppable Echo</title></head><body><h1>%s right back at ya!</h1></body></html>", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
