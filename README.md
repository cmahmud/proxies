# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 475
- HTTP: 283 alive / 123 gold
- HTTPS: 219 alive / 86 gold
- SOCKS4: 184 alive / 127 gold
- SOCKS5: 225 alive / 139 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17505
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
