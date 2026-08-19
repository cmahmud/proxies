# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 508
- HTTP: 388 alive / 149 gold
- HTTPS: 283 alive / 87 gold
- SOCKS4: 181 alive / 117 gold
- SOCKS5: 215 alive / 155 gold

## Historical pool

- Discovered: 118125
- Ever alive: 17781
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
