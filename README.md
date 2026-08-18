# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 256
- HTTP: 219 alive / 32 gold
- HTTPS: 126 alive / 8 gold
- SOCKS4: 231 alive / 124 gold
- SOCKS5: 228 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9106
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
