# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 410
- HTTP: 327 alive / 96 gold
- HTTPS: 196 alive / 26 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 267 alive / 149 gold

## Historical pool

- Discovered: 154713
- Ever alive: 29018
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
