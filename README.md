# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 444
- HTTP: 113 alive / 81 gold
- HTTPS: 110 alive / 27 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47560
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
