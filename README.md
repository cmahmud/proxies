# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 439
- HTTP: 97 alive / 79 gold
- HTTPS: 81 alive / 26 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47675
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
