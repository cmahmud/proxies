# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 383
- HTTP: 207 alive / 67 gold
- HTTPS: 122 alive / 13 gold
- SOCKS4: 185 alive / 144 gold
- SOCKS5: 217 alive / 159 gold

## Historical pool

- Discovered: 146589
- Ever alive: 25659
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
