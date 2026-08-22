# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 407
- HTTP: 271 alive / 84 gold
- HTTPS: 197 alive / 26 gold
- SOCKS4: 208 alive / 142 gold
- SOCKS5: 251 alive / 155 gold

## Historical pool

- Discovered: 163863
- Ever alive: 31985
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
