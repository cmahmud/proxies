# SyndProxy private pool

## Current pool

- Alive now: 1384
- Gold now: 590
- HTTP: 527 alive / 188 gold
- HTTPS: 369 alive / 96 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 248 alive / 159 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23540
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
