# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 405
- HTTP: 232 alive / 82 gold
- HTTPS: 153 alive / 23 gold
- SOCKS4: 207 alive / 144 gold
- SOCKS5: 255 alive / 156 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29344
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
