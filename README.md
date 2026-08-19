# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 484
- HTTP: 362 alive / 127 gold
- HTTPS: 253 alive / 78 gold
- SOCKS4: 195 alive / 124 gold
- SOCKS5: 238 alive / 155 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17865
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
