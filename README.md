# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 390
- HTTP: 117 alive / 58 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33510
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
