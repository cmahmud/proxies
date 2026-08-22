# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 422
- HTTP: 267 alive / 94 gold
- HTTPS: 172 alive / 27 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 167123
- Ever alive: 32544
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
