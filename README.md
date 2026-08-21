# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 405
- HTTP: 291 alive / 96 gold
- HTTPS: 219 alive / 24 gold
- SOCKS4: 243 alive / 155 gold
- SOCKS5: 218 alive / 130 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30835
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
