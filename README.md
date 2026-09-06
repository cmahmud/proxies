# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 401
- HTTP: 119 alive / 79 gold
- HTTPS: 63 alive / 19 gold
- SOCKS4: 167 alive / 147 gold
- SOCKS5: 184 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48054
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
