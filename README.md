# SyndProxy private pool

## Current pool

- Alive now: 1611
- Gold now: 589
- HTTP: 640 alive / 186 gold
- HTTPS: 506 alive / 92 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 246 alive / 167 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24014
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
