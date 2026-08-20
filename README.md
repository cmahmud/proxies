# SyndProxy private pool

## Current pool

- Alive now: 1508
- Gold now: 567
- HTTP: 602 alive / 191 gold
- HTTPS: 423 alive / 88 gold
- SOCKS4: 216 alive / 131 gold
- SOCKS5: 267 alive / 157 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23096
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
