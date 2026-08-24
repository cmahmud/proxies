# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 391
- HTTP: 134 alive / 56 gold
- HTTPS: 79 alive / 14 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33524
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
