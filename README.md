# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 213
- HTTP: 238 alive / 25 gold
- HTTPS: 140 alive / 8 gold
- SOCKS4: 184 alive / 95 gold
- SOCKS5: 218 alive / 85 gold

## Historical pool

- Discovered: 91714
- Ever alive: 8646
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
