# SyndProxy private pool

## Current pool

- Alive now: 1548
- Gold now: 644
- HTTP: 591 alive / 214 gold
- HTTPS: 486 alive / 108 gold
- SOCKS4: 218 alive / 152 gold
- SOCKS5: 253 alive / 170 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23973
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
