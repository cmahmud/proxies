# SyndProxy private pool

## Current pool

- Alive now: 1287
- Gold now: 596
- HTTP: 479 alive / 184 gold
- HTTPS: 335 alive / 111 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 235 alive / 156 gold

## Historical pool

- Discovered: 125593
- Ever alive: 19554
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
