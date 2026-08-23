# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 383
- HTTP: 86 alive / 57 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 174835
- Ever alive: 33118
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
