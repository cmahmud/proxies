# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 398
- HTTP: 398 alive / 92 gold
- HTTPS: 279 alive / 14 gold
- SOCKS4: 213 alive / 129 gold
- SOCKS5: 246 alive / 163 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21250
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
