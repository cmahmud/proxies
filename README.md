# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 266
- HTTP: 214 alive / 30 gold
- HTTPS: 192 alive / 4 gold
- SOCKS4: 222 alive / 120 gold
- SOCKS5: 241 alive / 112 gold

## Historical pool

- Discovered: 99162
- Ever alive: 12137
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
