# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 374
- HTTP: 296 alive / 71 gold
- HTTPS: 212 alive / 20 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 225 alive / 142 gold

## Historical pool

- Discovered: 149502
- Ever alive: 26730
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
