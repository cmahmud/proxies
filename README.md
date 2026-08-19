# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 487
- HTTP: 369 alive / 123 gold
- HTTPS: 227 alive / 74 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 258 alive / 150 gold

## Historical pool

- Discovered: 114274
- Ever alive: 16918
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
