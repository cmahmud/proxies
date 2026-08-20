# SyndProxy private pool

## Current pool

- Alive now: 1625
- Gold now: 645
- HTTP: 611 alive / 237 gold
- HTTPS: 509 alive / 122 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 267 alive / 141 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24659
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
