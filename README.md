# SyndProxy private pool

## Current pool

- Alive now: 1347
- Gold now: 604
- HTTP: 496 alive / 198 gold
- HTTPS: 394 alive / 99 gold
- SOCKS4: 215 alive / 145 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 138953
- Ever alive: 23404
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
