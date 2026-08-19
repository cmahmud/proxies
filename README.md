# SyndProxy private pool

## Current pool

- Alive now: 1314
- Gold now: 394
- HTTP: 468 alive / 96 gold
- HTTPS: 315 alive / 21 gold
- SOCKS4: 214 alive / 133 gold
- SOCKS5: 317 alive / 144 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22518
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
