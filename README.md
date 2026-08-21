# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 396
- HTTP: 245 alive / 86 gold
- HTTPS: 152 alive / 23 gold
- SOCKS4: 215 alive / 142 gold
- SOCKS5: 233 alive / 145 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29723
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
