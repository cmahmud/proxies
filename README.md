# SyndProxy private pool

## Current pool

- Alive now: 1540
- Gold now: 580
- HTTP: 623 alive / 182 gold
- HTTPS: 413 alive / 88 gold
- SOCKS4: 237 alive / 142 gold
- SOCKS5: 267 alive / 168 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23171
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
