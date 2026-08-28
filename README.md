# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 435
- HTTP: 114 alive / 83 gold
- HTTPS: 130 alive / 22 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42356
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
