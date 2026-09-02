# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 437
- HTTP: 112 alive / 78 gold
- HTTPS: 114 alive / 22 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47581
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
