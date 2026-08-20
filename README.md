# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 404
- HTTP: 180 alive / 85 gold
- HTTPS: 128 alive / 22 gold
- SOCKS4: 194 alive / 129 gold
- SOCKS5: 225 alive / 168 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27088
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
