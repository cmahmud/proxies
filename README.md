# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 466
- HTTP: 389 alive / 126 gold
- HTTPS: 271 alive / 86 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 179 alive / 111 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17464
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
