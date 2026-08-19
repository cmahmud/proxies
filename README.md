# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 514
- HTTP: 355 alive / 148 gold
- HTTPS: 233 alive / 89 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 203 alive / 129 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17624
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
