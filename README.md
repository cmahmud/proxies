# SyndProxy private pool

## Current pool

- Alive now: 1494
- Gold now: 596
- HTTP: 626 alive / 196 gold
- HTTPS: 405 alive / 94 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 250 alive / 165 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23105
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
