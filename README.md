# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 240
- HTTP: 235 alive / 29 gold
- HTTPS: 88 alive / 4 gold
- SOCKS4: 173 alive / 113 gold
- SOCKS5: 191 alive / 94 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10323
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
