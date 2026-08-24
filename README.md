# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 391
- HTTP: 116 alive / 59 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
