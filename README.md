# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 465
- HTTP: 306 alive / 120 gold
- HTTPS: 229 alive / 87 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 189 alive / 117 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17481
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
