# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 494
- HTTP: 322 alive / 147 gold
- HTTPS: 246 alive / 89 gold
- SOCKS4: 190 alive / 123 gold
- SOCKS5: 215 alive / 135 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17599
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
