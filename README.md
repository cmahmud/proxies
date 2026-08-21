# SyndProxy private pool

## Current pool

- Alive now: 1347
- Gold now: 443
- HTTP: 510 alive / 107 gold
- HTTPS: 342 alive / 33 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 267 alive / 165 gold

## Historical pool

- Discovered: 159270
- Ever alive: 30376
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
