# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 395
- HTTP: 290 alive / 91 gold
- HTTPS: 189 alive / 25 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 206 alive / 134 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32343
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
