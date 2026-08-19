# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 509
- HTTP: 353 alive / 159 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 215 alive / 142 gold
- SOCKS5: 204 alive / 118 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18373
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
