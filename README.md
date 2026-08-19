# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 464
- HTTP: 366 alive / 128 gold
- HTTPS: 264 alive / 80 gold
- SOCKS4: 210 alive / 141 gold
- SOCKS5: 206 alive / 115 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17456
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
