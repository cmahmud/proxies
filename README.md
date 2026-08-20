# SyndProxy private pool

## Current pool

- Alive now: 1424
- Gold now: 572
- HTTP: 568 alive / 188 gold
- HTTPS: 381 alive / 89 gold
- SOCKS4: 214 alive / 132 gold
- SOCKS5: 261 alive / 163 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23086
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
