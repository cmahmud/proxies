# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 478
- HTTP: 320 alive / 123 gold
- HTTPS: 220 alive / 70 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 249 alive / 147 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16873
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
