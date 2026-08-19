# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 523
- HTTP: 411 alive / 151 gold
- HTTPS: 284 alive / 89 gold
- SOCKS4: 225 alive / 148 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17734
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
