# SyndProxy private pool

## Current pool

- Alive now: 651
- Gold now: 381
- HTTP: 152 alive / 70 gold
- HTTPS: 97 alive / 16 gold
- SOCKS4: 196 alive / 153 gold
- SOCKS5: 206 alive / 142 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25699
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
