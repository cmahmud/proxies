# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 432
- HTTP: 107 alive / 74 gold
- HTTPS: 101 alive / 22 gold
- SOCKS4: 175 alive / 165 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47603
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
