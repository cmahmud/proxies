# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 389
- HTTP: 234 alive / 81 gold
- HTTPS: 273 alive / 26 gold
- SOCKS4: 215 alive / 145 gold
- SOCKS5: 209 alive / 137 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31869
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
