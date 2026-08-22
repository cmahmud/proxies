# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 420
- HTTP: 215 alive / 95 gold
- HTTPS: 135 alive / 29 gold
- SOCKS4: 214 alive / 132 gold
- SOCKS5: 248 alive / 164 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31953
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
