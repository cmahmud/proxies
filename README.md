# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 447
- HTTP: 123 alive / 80 gold
- HTTPS: 134 alive / 35 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44656
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
