# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 268
- HTTP: 317 alive / 45 gold
- HTTPS: 172 alive / 11 gold
- SOCKS4: 211 alive / 110 gold
- SOCKS5: 219 alive / 102 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14428
- Ever gold: 461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
