# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 416
- HTTP: 349 alive / 94 gold
- HTTPS: 267 alive / 32 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 242 alive / 156 gold

## Historical pool

- Discovered: 161018
- Ever alive: 31104
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
