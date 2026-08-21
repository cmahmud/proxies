# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 382
- HTTP: 252 alive / 69 gold
- HTTPS: 195 alive / 18 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 230 alive / 152 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29572
- Ever gold: 1130

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
