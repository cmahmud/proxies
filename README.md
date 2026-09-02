# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 439
- HTTP: 114 alive / 76 gold
- HTTPS: 108 alive / 27 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47566
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
