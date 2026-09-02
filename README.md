# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 437
- HTTP: 124 alive / 76 gold
- HTTPS: 121 alive / 23 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47609
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
