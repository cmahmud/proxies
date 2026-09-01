# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 442
- HTTP: 112 alive / 80 gold
- HTTPS: 74 alive / 30 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47012
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
