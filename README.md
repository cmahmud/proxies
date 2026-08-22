# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 417
- HTTP: 325 alive / 89 gold
- HTTPS: 252 alive / 26 gold
- SOCKS4: 214 alive / 144 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32082
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
