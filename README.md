# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 491
- HTTP: 325 alive / 145 gold
- HTTPS: 247 alive / 89 gold
- SOCKS4: 198 alive / 123 gold
- SOCKS5: 217 alive / 134 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17599
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
