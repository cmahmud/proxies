# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 444
- HTTP: 295 alive / 123 gold
- HTTPS: 193 alive / 46 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 230 alive / 134 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16782
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
