# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 375
- HTTP: 109 alive / 48 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33539
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
