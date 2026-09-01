# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 459
- HTTP: 124 alive / 81 gold
- HTTPS: 124 alive / 37 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 194 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46759
- Ever gold: 1450

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
