# SyndProxy private pool

## Current pool

- Alive now: 1432
- Gold now: 588
- HTTP: 602 alive / 197 gold
- HTTPS: 389 alive / 99 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 136253
- Ever alive: 22780
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
