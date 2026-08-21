# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 423
- HTTP: 343 alive / 105 gold
- HTTPS: 199 alive / 32 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 236 alive / 147 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30714
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
