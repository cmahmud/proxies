# SyndProxy private pool

## Current pool

- Alive now: 1488
- Gold now: 570
- HTTP: 595 alive / 193 gold
- HTTPS: 410 alive / 86 gold
- SOCKS4: 216 alive / 129 gold
- SOCKS5: 267 alive / 162 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23095
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
