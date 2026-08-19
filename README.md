# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 458
- HTTP: 372 alive / 123 gold
- HTTPS: 287 alive / 78 gold
- SOCKS4: 214 alive / 142 gold
- SOCKS5: 189 alive / 115 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17462
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
