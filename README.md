# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 364
- HTTP: 312 alive / 72 gold
- HTTPS: 228 alive / 18 gold
- SOCKS4: 256 alive / 153 gold
- SOCKS5: 215 alive / 121 gold

## Historical pool

- Discovered: 110860
- Ever alive: 15944
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
