# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 434
- HTTP: 138 alive / 82 gold
- HTTPS: 103 alive / 20 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34444
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
