# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 376
- HTTP: 190 alive / 82 gold
- HTTPS: 148 alive / 20 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 213 alive / 131 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26619
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
