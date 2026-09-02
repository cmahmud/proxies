# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 453
- HTTP: 101 alive / 81 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 189 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47544
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
