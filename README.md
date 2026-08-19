# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 464
- HTTP: 398 alive / 126 gold
- HTTPS: 252 alive / 67 gold
- SOCKS4: 210 alive / 129 gold
- SOCKS5: 253 alive / 142 gold

## Historical pool

- Discovered: 117103
- Ever alive: 17143
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
