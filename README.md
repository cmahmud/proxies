# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 387
- HTTP: 220 alive / 78 gold
- HTTPS: 124 alive / 17 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25969
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
