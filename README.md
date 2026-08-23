# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 383
- HTTP: 87 alive / 55 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33106
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
