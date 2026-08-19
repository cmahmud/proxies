# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 472
- HTTP: 298 alive / 119 gold
- HTTPS: 219 alive / 86 gold
- SOCKS4: 183 alive / 129 gold
- SOCKS5: 221 alive / 138 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17512
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
