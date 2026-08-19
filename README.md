# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 469
- HTTP: 298 alive / 121 gold
- HTTPS: 212 alive / 86 gold
- SOCKS4: 177 alive / 128 gold
- SOCKS5: 211 alive / 134 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17521
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
