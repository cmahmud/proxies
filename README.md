# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 387
- HTTP: 100 alive / 54 gold
- HTTPS: 72 alive / 13 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33531
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
