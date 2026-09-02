# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 432
- HTTP: 99 alive / 74 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47666
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
