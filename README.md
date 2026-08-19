# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 470
- HTTP: 387 alive / 120 gold
- HTTPS: 265 alive / 74 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 247 alive / 134 gold

## Historical pool

- Discovered: 113533
- Ever alive: 16433
- Ever gold: 619

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
