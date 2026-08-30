# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 430
- HTTP: 151 alive / 87 gold
- HTTPS: 95 alive / 31 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 210 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44007
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
