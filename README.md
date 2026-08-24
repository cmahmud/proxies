# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 389
- HTTP: 113 alive / 53 gold
- HTTPS: 52 alive / 13 gold
- SOCKS4: 180 alive / 157 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33383
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
