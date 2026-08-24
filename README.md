# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 385
- HTTP: 103 alive / 52 gold
- HTTPS: 35 alive / 13 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33407
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
