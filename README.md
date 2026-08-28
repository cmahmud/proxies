# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 390
- HTTP: 94 alive / 67 gold
- HTTPS: 71 alive / 10 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 171 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43186
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
