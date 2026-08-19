# SyndProxy private pool

## Current pool

- Alive now: 1209
- Gold now: 403
- HTTP: 405 alive / 94 gold
- HTTPS: 267 alive / 14 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 305 alive / 155 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20989
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
