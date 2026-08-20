# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 383
- HTTP: 214 alive / 77 gold
- HTTPS: 192 alive / 20 gold
- SOCKS4: 202 alive / 148 gold
- SOCKS5: 215 alive / 138 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26834
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
