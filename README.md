# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 394
- HTTP: 121 alive / 60 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33527
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
