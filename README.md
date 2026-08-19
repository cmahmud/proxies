# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 361
- HTTP: 386 alive / 73 gold
- HTTPS: 234 alive / 12 gold
- SOCKS4: 215 alive / 129 gold
- SOCKS5: 251 alive / 147 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20364
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
