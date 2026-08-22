# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 418
- HTTP: 319 alive / 100 gold
- HTTPS: 223 alive / 30 gold
- SOCKS4: 205 alive / 135 gold
- SOCKS5: 228 alive / 153 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31088
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
