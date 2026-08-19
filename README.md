# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 340
- HTTP: 314 alive / 61 gold
- HTTPS: 249 alive / 16 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 203 alive / 119 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15383
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
