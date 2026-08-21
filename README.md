# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 353
- HTTP: 267 alive / 93 gold
- HTTPS: 163 alive / 21 gold
- SOCKS4: 196 alive / 134 gold
- SOCKS5: 200 alive / 105 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28952
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
