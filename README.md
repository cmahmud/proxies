# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 459
- HTTP: 132 alive / 92 gold
- HTTPS: 119 alive / 36 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44813
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
