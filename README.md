# SyndProxy private pool

## Current pool

- Alive now: 1527
- Gold now: 392
- HTTP: 561 alive / 104 gold
- HTTPS: 394 alive / 20 gold
- SOCKS4: 253 alive / 124 gold
- SOCKS5: 319 alive / 144 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22494
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
