# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 403
- HTTP: 286 alive / 94 gold
- HTTPS: 192 alive / 29 gold
- SOCKS4: 233 alive / 155 gold
- SOCKS5: 216 alive / 125 gold

## Historical pool

- Discovered: 160987
- Ever alive: 30866
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
