# SyndProxy private pool

## Current pool

- Alive now: 1439
- Gold now: 427
- HTTP: 550 alive / 110 gold
- HTTPS: 342 alive / 23 gold
- SOCKS4: 229 alive / 140 gold
- SOCKS5: 318 alive / 154 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22659
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
