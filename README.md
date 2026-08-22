# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 423
- HTTP: 220 alive / 92 gold
- HTTPS: 141 alive / 28 gold
- SOCKS4: 185 alive / 135 gold
- SOCKS5: 232 alive / 168 gold

## Historical pool

- Discovered: 162702
- Ever alive: 31457
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
