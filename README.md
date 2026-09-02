# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 440
- HTTP: 113 alive / 78 gold
- HTTPS: 114 alive / 25 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47560
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
