# SyndProxy private pool

## Current pool

- Alive now: 1263
- Gold now: 425
- HTTP: 461 alive / 103 gold
- HTTPS: 295 alive / 26 gold
- SOCKS4: 200 alive / 141 gold
- SOCKS5: 307 alive / 155 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22644
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
