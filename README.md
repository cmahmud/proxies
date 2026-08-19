# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 524
- HTTP: 353 alive / 153 gold
- HTTPS: 242 alive / 91 gold
- SOCKS4: 215 alive / 145 gold
- SOCKS5: 214 alive / 135 gold

## Historical pool

- Discovered: 127362
- Ever alive: 19896
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
