# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 446
- HTTP: 99 alive / 78 gold
- HTTPS: 108 alive / 29 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47535
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
