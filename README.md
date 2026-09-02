# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 447
- HTTP: 135 alive / 79 gold
- HTTPS: 107 alive / 30 gold
- SOCKS4: 187 alive / 165 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47633
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
