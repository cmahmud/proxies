# SyndProxy private pool

## Current pool

- Alive now: 1358
- Gold now: 431
- HTTP: 501 alive / 95 gold
- HTTPS: 296 alive / 24 gold
- SOCKS4: 242 alive / 149 gold
- SOCKS5: 319 alive / 163 gold

## Historical pool

- Discovered: 136218
- Ever alive: 22439
- Ever gold: 899

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
