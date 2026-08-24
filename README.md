# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 391
- HTTP: 119 alive / 55 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33530
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
