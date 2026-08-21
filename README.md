# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 409
- HTTP: 323 alive / 99 gold
- HTTPS: 219 alive / 29 gold
- SOCKS4: 224 alive / 155 gold
- SOCKS5: 235 alive / 126 gold

## Historical pool

- Discovered: 160353
- Ever alive: 30815
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
