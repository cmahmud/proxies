# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 373
- HTTP: 103 alive / 49 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33539
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
