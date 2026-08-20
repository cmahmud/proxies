# SyndProxy private pool

## Current pool

- Alive now: 1459
- Gold now: 587
- HTTP: 620 alive / 197 gold
- HTTPS: 388 alive / 98 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 229 alive / 151 gold

## Historical pool

- Discovered: 136253
- Ever alive: 22780
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
