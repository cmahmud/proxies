# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 262
- HTTP: 410 alive / 32 gold
- HTTPS: 174 alive / 4 gold
- SOCKS4: 225 alive / 119 gold
- SOCKS5: 228 alive / 107 gold

## Historical pool

- Discovered: 95405
- Ever alive: 11000
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
