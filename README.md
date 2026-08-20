# SyndProxy private pool

## Current pool

- Alive now: 685
- Gold now: 388
- HTTP: 190 alive / 69 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 183 alive / 150 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25750
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
