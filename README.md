# SyndProxy private pool

## Current pool

- Alive now: 1382
- Gold now: 430
- HTTP: 534 alive / 110 gold
- HTTPS: 312 alive / 24 gold
- SOCKS4: 225 alive / 141 gold
- SOCKS5: 311 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22651
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
