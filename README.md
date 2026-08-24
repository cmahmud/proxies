# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 390
- HTTP: 114 alive / 53 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 204 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33382
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
