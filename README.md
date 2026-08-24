# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 437
- HTTP: 140 alive / 81 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34535
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
