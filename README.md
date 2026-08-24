# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 395
- HTTP: 194 alive / 61 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33513
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
