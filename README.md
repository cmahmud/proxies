# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 405
- HTTP: 352 alive / 78 gold
- HTTPS: 207 alive / 27 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 156566
- Ever alive: 29561
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
