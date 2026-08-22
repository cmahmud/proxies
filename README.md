# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 385
- HTTP: 267 alive / 89 gold
- HTTPS: 203 alive / 25 gold
- SOCKS4: 214 alive / 142 gold
- SOCKS5: 238 alive / 129 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31789
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
