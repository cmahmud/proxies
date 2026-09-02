# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 448
- HTTP: 96 alive / 79 gold
- HTTPS: 102 alive / 30 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47540
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
