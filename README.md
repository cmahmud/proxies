# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 276
- HTTP: 270 alive / 52 gold
- HTTPS: 173 alive / 11 gold
- SOCKS4: 218 alive / 111 gold
- SOCKS5: 216 alive / 102 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
