# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 457
- HTTP: 130 alive / 90 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44808
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
