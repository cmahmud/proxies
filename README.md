# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 425
- HTTP: 270 alive / 98 gold
- HTTPS: 189 alive / 30 gold
- SOCKS4: 186 alive / 140 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31073
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
