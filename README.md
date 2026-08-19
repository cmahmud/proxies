# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 393
- HTTP: 342 alive / 75 gold
- HTTPS: 215 alive / 14 gold
- SOCKS4: 248 alive / 143 gold
- SOCKS5: 248 alive / 161 gold

## Historical pool

- Discovered: 131100
- Ever alive: 20526
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
