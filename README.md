# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 508
- HTTP: 393 alive / 146 gold
- HTTPS: 297 alive / 89 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 209 alive / 129 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17699
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
