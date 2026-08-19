# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 381
- HTTP: 365 alive / 93 gold
- HTTPS: 227 alive / 14 gold
- SOCKS4: 234 alive / 138 gold
- SOCKS5: 287 alive / 136 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20998
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
