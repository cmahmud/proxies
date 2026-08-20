# SyndProxy private pool

## Current pool

- Alive now: 681
- Gold now: 381
- HTTP: 183 alive / 70 gold
- HTTPS: 105 alive / 16 gold
- SOCKS4: 199 alive / 153 gold
- SOCKS5: 194 alive / 142 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25704
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
