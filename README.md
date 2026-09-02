# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 437
- HTTP: 118 alive / 76 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47600
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
