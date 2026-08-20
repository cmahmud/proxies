# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 354
- HTTP: 198 alive / 63 gold
- HTTPS: 140 alive / 17 gold
- SOCKS4: 198 alive / 132 gold
- SOCKS5: 204 alive / 142 gold

## Historical pool

- Discovered: 145551
- Ever alive: 25420
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
