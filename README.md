# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 426
- HTTP: 140 alive / 75 gold
- HTTPS: 86 alive / 22 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33907
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
