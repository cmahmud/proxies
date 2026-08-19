# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 475
- HTTP: 333 alive / 142 gold
- HTTPS: 263 alive / 87 gold
- SOCKS4: 203 alive / 118 gold
- SOCKS5: 220 alive / 128 gold

## Historical pool

- Discovered: 117155
- Ever alive: 17571
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
