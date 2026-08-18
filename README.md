# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 213
- HTTP: 242 alive / 25 gold
- HTTPS: 150 alive / 8 gold
- SOCKS4: 184 alive / 95 gold
- SOCKS5: 219 alive / 85 gold

## Historical pool

- Discovered: 91714
- Ever alive: 8646
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
