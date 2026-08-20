# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 378
- HTTP: 213 alive / 70 gold
- HTTPS: 105 alive / 22 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 208 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25424
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
