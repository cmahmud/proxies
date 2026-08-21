# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 373
- HTTP: 203 alive / 80 gold
- HTTPS: 134 alive / 25 gold
- SOCKS4: 207 alive / 130 gold
- SOCKS5: 226 alive / 138 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29352
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
