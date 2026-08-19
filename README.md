# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 488
- HTTP: 326 alive / 149 gold
- HTTPS: 239 alive / 87 gold
- SOCKS4: 215 alive / 120 gold
- SOCKS5: 229 alive / 132 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17576
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
