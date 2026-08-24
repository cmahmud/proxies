# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 395
- HTTP: 182 alive / 61 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33518
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
