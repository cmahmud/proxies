# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 451
- HTTP: 107 alive / 81 gold
- HTTPS: 112 alive / 31 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47547
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
