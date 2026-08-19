# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 486
- HTTP: 364 alive / 129 gold
- HTTPS: 256 alive / 79 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 233 alive / 154 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
