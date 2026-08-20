# SyndProxy private pool

## Current pool

- Alive now: 653
- Gold now: 376
- HTTP: 158 alive / 67 gold
- HTTPS: 92 alive / 15 gold
- SOCKS4: 200 alive / 153 gold
- SOCKS5: 203 alive / 141 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25700
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
