# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 517
- HTTP: 397 alive / 145 gold
- HTTPS: 250 alive / 89 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 212 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17717
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
