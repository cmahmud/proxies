# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 461
- HTTP: 143 alive / 93 gold
- HTTPS: 115 alive / 34 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46874
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
