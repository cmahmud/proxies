# SyndProxy private pool

## Current pool

- Alive now: 1438
- Gold now: 395
- HTTP: 501 alive / 92 gold
- HTTPS: 359 alive / 20 gold
- SOCKS4: 247 alive / 129 gold
- SOCKS5: 331 alive / 154 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22026
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
