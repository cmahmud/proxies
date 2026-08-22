# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 398
- HTTP: 312 alive / 76 gold
- HTTPS: 210 alive / 21 gold
- SOCKS4: 209 alive / 150 gold
- SOCKS5: 226 alive / 151 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32297
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
