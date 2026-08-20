# SyndProxy private pool

## Current pool

- Alive now: 1432
- Gold now: 619
- HTTP: 549 alive / 219 gold
- HTTPS: 431 alive / 115 gold
- SOCKS4: 216 alive / 136 gold
- SOCKS5: 236 alive / 149 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23801
- Ever gold: 961

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
