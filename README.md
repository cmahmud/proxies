# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 396
- HTTP: 420 alive / 90 gold
- HTTPS: 314 alive / 15 gold
- SOCKS4: 219 alive / 129 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21258
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
