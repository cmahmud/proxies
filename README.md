# SyndProxy private pool

## Current pool

- Alive now: 1560
- Gold now: 650
- HTTP: 590 alive / 213 gold
- HTTPS: 493 alive / 112 gold
- SOCKS4: 233 alive / 155 gold
- SOCKS5: 244 alive / 170 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23967
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
