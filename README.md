# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 366
- HTTP: 233 alive / 88 gold
- HTTPS: 161 alive / 16 gold
- SOCKS4: 202 alive / 138 gold
- SOCKS5: 208 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18292
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
