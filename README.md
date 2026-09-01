# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 459
- HTTP: 138 alive / 93 gold
- HTTPS: 117 alive / 33 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46874
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
