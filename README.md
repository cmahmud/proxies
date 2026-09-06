# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 326
- HTTP: 80 alive / 56 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 153 alive / 136 gold
- SOCKS5: 161 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48395
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
