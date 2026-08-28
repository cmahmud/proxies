# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 425
- HTTP: 120 alive / 80 gold
- HTTPS: 119 alive / 22 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 195 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42386
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
