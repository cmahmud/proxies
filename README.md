# SyndProxy private pool

## Current pool

- Alive now: 752
- Gold now: 249
- HTTP: 195 alive / 28 gold
- HTTPS: 102 alive / 8 gold
- SOCKS4: 235 alive / 121 gold
- SOCKS5: 220 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9106
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
