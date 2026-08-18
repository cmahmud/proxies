# SyndProxy private pool

## Current pool

- Alive now: 657
- Gold now: 250
- HTTP: 218 alive / 28 gold
- HTTPS: 86 alive / 10 gold
- SOCKS4: 178 alive / 127 gold
- SOCKS5: 175 alive / 85 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9757
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
