# SyndProxy private pool

## Current pool

- Alive now: 1117
- Gold now: 432
- HTTP: 362 alive / 111 gold
- HTTPS: 237 alive / 30 gold
- SOCKS4: 253 alive / 150 gold
- SOCKS5: 265 alive / 141 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30777
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
