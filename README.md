# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 444
- HTTP: 115 alive / 80 gold
- HTTPS: 106 alive / 27 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47560
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
