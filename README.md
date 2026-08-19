# SyndProxy private pool

## Current pool

- Alive now: 1100
- Gold now: 436
- HTTP: 389 alive / 124 gold
- HTTPS: 247 alive / 41 gold
- SOCKS4: 212 alive / 128 gold
- SOCKS5: 252 alive / 143 gold

## Historical pool

- Discovered: 117103
- Ever alive: 17139
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
