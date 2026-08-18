# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 248
- HTTP: 193 alive / 28 gold
- HTTPS: 102 alive / 7 gold
- SOCKS4: 228 alive / 121 gold
- SOCKS5: 216 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9106
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
