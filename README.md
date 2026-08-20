# SyndProxy private pool

## Current pool

- Alive now: 1490
- Gold now: 597
- HTTP: 621 alive / 197 gold
- HTTPS: 407 alive / 94 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 250 alive / 165 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23105
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
