# SyndProxy private pool

## Current pool

- Alive now: 1381
- Gold now: 595
- HTTP: 538 alive / 192 gold
- HTTPS: 368 alive / 100 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 256 alive / 166 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23114
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
