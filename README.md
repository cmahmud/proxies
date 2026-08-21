# SyndProxy private pool

## Current pool

- Alive now: 1361
- Gold now: 457
- HTTP: 508 alive / 114 gold
- HTTPS: 354 alive / 32 gold
- SOCKS4: 240 alive / 153 gold
- SOCKS5: 259 alive / 158 gold

## Historical pool

- Discovered: 160009
- Ever alive: 30506
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
