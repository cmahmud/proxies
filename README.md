# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 389
- HTTP: 92 alive / 53 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33393
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
