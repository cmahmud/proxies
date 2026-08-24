# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 379
- HTTP: 101 alive / 47 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33537
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
