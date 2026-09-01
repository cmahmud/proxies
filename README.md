# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 427
- HTTP: 102 alive / 71 gold
- HTTPS: 66 alive / 27 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47027
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
