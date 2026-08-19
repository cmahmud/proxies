# SyndProxy private pool

## Current pool

- Alive now: 1211
- Gold now: 405
- HTTP: 396 alive / 87 gold
- HTTPS: 267 alive / 17 gold
- SOCKS4: 240 alive / 148 gold
- SOCKS5: 308 alive / 153 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21986
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
