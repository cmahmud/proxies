# SyndProxy private pool

## Current pool

- Alive now: 1880
- Gold now: 657
- HTTP: 717 alive / 234 gold
- HTTPS: 617 alive / 121 gold
- SOCKS4: 245 alive / 146 gold
- SOCKS5: 301 alive / 156 gold

## Historical pool

- Discovered: 142693
- Ever alive: 24296
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
