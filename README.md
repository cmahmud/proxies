# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 492
- HTTP: 139 alive / 103 gold
- HTTPS: 127 alive / 51 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 202 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45009
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
