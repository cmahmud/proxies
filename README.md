# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 241
- HTTP: 341 alive / 39 gold
- HTTPS: 134 alive / 7 gold
- SOCKS4: 211 alive / 126 gold
- SOCKS5: 216 alive / 69 gold

## Historical pool

- Discovered: 94342
- Ever alive: 9615
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
