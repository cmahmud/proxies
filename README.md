# SyndProxy private pool

## Current pool

- Alive now: 1382
- Gold now: 588
- HTTP: 513 alive / 191 gold
- HTTPS: 394 alive / 94 gold
- SOCKS4: 232 alive / 147 gold
- SOCKS5: 243 alive / 156 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23557
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
