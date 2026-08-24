# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 390
- HTTP: 111 alive / 59 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 176 alive / 154 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
