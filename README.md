# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 485
- HTTP: 369 alive / 136 gold
- HTTPS: 255 alive / 80 gold
- SOCKS4: 209 alive / 120 gold
- SOCKS5: 223 alive / 149 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
