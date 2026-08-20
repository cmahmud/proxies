# SyndProxy private pool

## Current pool

- Alive now: 1431
- Gold now: 568
- HTTP: 569 alive / 188 gold
- HTTPS: 383 alive / 89 gold
- SOCKS4: 215 alive / 131 gold
- SOCKS5: 264 alive / 160 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23086
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
