# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 515
- HTTP: 331 alive / 150 gold
- HTTPS: 261 alive / 90 gold
- SOCKS4: 215 alive / 148 gold
- SOCKS5: 202 alive / 127 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17612
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
