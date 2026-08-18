# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 246
- HTTP: 349 alive / 34 gold
- HTTPS: 148 alive / 7 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 150 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13591
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
