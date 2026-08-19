# SyndProxy private pool

## Current pool

- Alive now: 1418
- Gold now: 389
- HTTP: 506 alive / 89 gold
- HTTPS: 359 alive / 18 gold
- SOCKS4: 231 alive / 129 gold
- SOCKS5: 322 alive / 153 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22022
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
