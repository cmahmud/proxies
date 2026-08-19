# SyndProxy private pool

## Current pool

- Alive now: 1256
- Gold now: 389
- HTTP: 427 alive / 95 gold
- HTTPS: 308 alive / 17 gold
- SOCKS4: 236 alive / 138 gold
- SOCKS5: 285 alive / 139 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21603
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
