# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 507
- HTTP: 374 alive / 149 gold
- HTTPS: 256 alive / 88 gold
- SOCKS4: 180 alive / 117 gold
- SOCKS5: 217 alive / 153 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17741
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
