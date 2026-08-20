# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 427
- HTTP: 327 alive / 99 gold
- HTTPS: 238 alive / 26 gold
- SOCKS4: 239 alive / 152 gold
- SOCKS5: 252 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25190
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
