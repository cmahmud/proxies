# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 363
- HTTP: 299 alive / 71 gold
- HTTPS: 222 alive / 18 gold
- SOCKS4: 253 alive / 153 gold
- SOCKS5: 219 alive / 121 gold

## Historical pool

- Discovered: 110860
- Ever alive: 15938
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
