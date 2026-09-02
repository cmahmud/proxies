# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 433
- HTTP: 98 alive / 75 gold
- HTTPS: 97 alive / 22 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47670
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
