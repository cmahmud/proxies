# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 453
- HTTP: 101 alive / 81 gold
- HTTPS: 99 alive / 31 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 190 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47544
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
