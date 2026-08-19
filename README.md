# SyndProxy private pool

## Current pool

- Alive now: 1244
- Gold now: 403
- HTTP: 417 alive / 89 gold
- HTTPS: 282 alive / 16 gold
- SOCKS4: 242 alive / 149 gold
- SOCKS5: 303 alive / 149 gold

## Historical pool

- Discovered: 134541
- Ever alive: 21993
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
