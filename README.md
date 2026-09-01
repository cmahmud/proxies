# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 459
- HTTP: 138 alive / 86 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 191 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46720
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
