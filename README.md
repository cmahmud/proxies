# SyndProxy private pool

## Current pool

- Alive now: 1092
- Gold now: 447
- HTTP: 371 alive / 114 gold
- HTTPS: 264 alive / 32 gold
- SOCKS4: 201 alive / 155 gold
- SOCKS5: 256 alive / 146 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28634
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
