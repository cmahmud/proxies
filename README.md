# SyndProxy private pool

## Current pool

- Alive now: 665
- Gold now: 374
- HTTP: 170 alive / 61 gold
- HTTPS: 105 alive / 17 gold
- SOCKS4: 196 alive / 153 gold
- SOCKS5: 194 alive / 143 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25704
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
