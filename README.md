# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 395
- HTTP: 218 alive / 77 gold
- HTTPS: 155 alive / 16 gold
- SOCKS4: 192 alive / 146 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29323
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
