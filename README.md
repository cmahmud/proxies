# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 377
- HTTP: 340 alive / 88 gold
- HTTPS: 245 alive / 24 gold
- SOCKS4: 159 alive / 103 gold
- SOCKS5: 255 alive / 162 gold

## Historical pool

- Discovered: 166625
- Ever alive: 32458
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
