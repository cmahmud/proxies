# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 422
- HTTP: 117 alive / 72 gold
- HTTPS: 64 alive / 21 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44387
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
