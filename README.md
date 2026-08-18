# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 284
- HTTP: 241 alive / 25 gold
- HTTPS: 148 alive / 4 gold
- SOCKS4: 239 alive / 142 gold
- SOCKS5: 230 alive / 113 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12338
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
