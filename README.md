# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 485
- HTTP: 360 alive / 128 gold
- HTTPS: 255 alive / 79 gold
- SOCKS4: 205 alive / 124 gold
- SOCKS5: 235 alive / 154 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
