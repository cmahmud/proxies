# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 447
- HTTP: 365 alive / 107 gold
- HTTPS: 254 alive / 32 gold
- SOCKS4: 206 alive / 147 gold
- SOCKS5: 279 alive / 161 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28663
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
