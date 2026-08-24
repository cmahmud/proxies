# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 389
- HTTP: 90 alive / 49 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33544
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
