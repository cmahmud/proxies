# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 472
- HTTP: 123 alive / 95 gold
- HTTPS: 112 alive / 38 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 203 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46377
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
