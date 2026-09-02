# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 433
- HTTP: 122 alive / 76 gold
- HTTPS: 99 alive / 20 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47574
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
