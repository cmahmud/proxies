# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 438
- HTTP: 98 alive / 78 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47593
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
