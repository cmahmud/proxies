# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 213
- HTTP: 247 alive / 26 gold
- HTTPS: 148 alive / 8 gold
- SOCKS4: 185 alive / 95 gold
- SOCKS5: 219 alive / 84 gold

## Historical pool

- Discovered: 91714
- Ever alive: 8646
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
