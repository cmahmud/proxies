# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 448
- HTTP: 427 alive / 106 gold
- HTTPS: 291 alive / 29 gold
- SOCKS4: 211 alive / 152 gold
- SOCKS5: 261 alive / 161 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28577
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
