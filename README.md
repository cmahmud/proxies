# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 460
- HTTP: 124 alive / 88 gold
- HTTPS: 123 alive / 34 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 195 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46772
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
