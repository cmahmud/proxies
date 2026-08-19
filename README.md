# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 494
- HTTP: 398 alive / 152 gold
- HTTPS: 268 alive / 87 gold
- SOCKS4: 178 alive / 114 gold
- SOCKS5: 204 alive / 141 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17741
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
