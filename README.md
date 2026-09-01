# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 439
- HTTP: 113 alive / 79 gold
- HTTPS: 80 alive / 29 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47012
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
