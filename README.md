# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 387
- HTTP: 158 alive / 68 gold
- HTTPS: 132 alive / 18 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 207 alive / 156 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26014
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
