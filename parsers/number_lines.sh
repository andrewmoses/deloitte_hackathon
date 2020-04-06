git -c log.showSignature=false log master --use-mailmap $_merges --numstat \
        --pretty="format:commit %H%nAuthor: %aN <%aE>%nDate:   %ad%n%n%w(0,4,4)%B%n" \
        $_since $_until $_pathspec | LC_ALL=C awk '
        function printStats(author) {
        printf "\t%s:\n", author
        if(more["total"] > 0) {
            printf "\t  insertions:    %d (%.0f%%)\n", more[author], \
                (more[author] / more["total"] * 100)
        }
        if(less["total"] > 0) {
            printf "\t  deletions:     %d (%.0f%%)\n", less[author], \
                (less[author] / less["total"] * 100)
        }
        if(file["total"] > 0) {
            printf "\t  files:         %d (%.0f%%)\n", file[author], \
                (file[author] / file["total"] * 100)
        }
        if(commits["total"] > 0) {
            printf "\t  commits:       %d (%.0f%%)\n", commits[author], \
                (commits[author] / commits["total"] * 100)
        }
        if (first[author] != "") {
            printf "\t  lines changed: %s\n", more[author] + less[author]
            printf "\t  first commit:  %s\n", first[author]
            printf "\t  last commit:   %s\n", last[author]
        }
        printf "\n"
        }
        /^Author:/ {
        $1 = ""
        author = $0
        commits[author] += 1
        commits["total"] += 1
        }
        /^Date:/ {
        $1="";
        first[author] = substr($0, 2)
        if(last[author] == "" ) { last[author] = first[author] }
        }
        /^[0-9]/ {
        more[author] += $1
        less[author] += $2
        file[author] += 1
        more["total"]  += $1
        less["total"]  += $2
        file["total"]  += 1
        }
        END {
        for (author in commits) {
            if (author != "total") {
            printStats(author)
            }
        }
        printStats("total")
        }'
