# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 465
- HTTP: 136 alive / 96 gold
- HTTPS: 118 alive / 38 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44838
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
