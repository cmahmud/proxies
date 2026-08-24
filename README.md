# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 381
- HTTP: 86 alive / 49 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33555
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
