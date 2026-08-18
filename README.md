# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 273
- HTTP: 274 alive / 51 gold
- HTTPS: 191 alive / 11 gold
- SOCKS4: 212 alive / 110 gold
- SOCKS5: 217 alive / 101 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
