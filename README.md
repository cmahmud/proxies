# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 404
- HTTP: 115 alive / 79 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 165 alive / 147 gold
- SOCKS5: 184 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48054
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
