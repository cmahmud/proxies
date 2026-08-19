# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 465
- HTTP: 394 alive / 129 gold
- HTTPS: 267 alive / 80 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 204 alive / 115 gold

## Historical pool

- Discovered: 117128
- Ever alive: 17456
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
