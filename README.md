# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 393
- HTTP: 209 alive / 90 gold
- HTTPS: 114 alive / 26 gold
- SOCKS4: 183 alive / 121 gold
- SOCKS5: 237 alive / 156 gold

## Historical pool

- Discovered: 156423
- Ever alive: 29475
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
