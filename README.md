# SyndProxy private pool

## Current pool

- Alive now: 1267
- Gold now: 500
- HTTP: 481 alive / 162 gold
- HTTPS: 338 alive / 50 gold
- SOCKS4: 209 alive / 134 gold
- SOCKS5: 239 alive / 154 gold

## Historical pool

- Discovered: 125701
- Ever alive: 19674
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
