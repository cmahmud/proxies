# SyndProxy private pool

## Current pool

- Alive now: 1369
- Gold now: 417
- HTTP: 521 alive / 86 gold
- HTTPS: 332 alive / 16 gold
- SOCKS4: 268 alive / 157 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20805
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
