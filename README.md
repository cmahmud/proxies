# SyndProxy private pool

## Current pool

- Alive now: 493
- Gold now: 152
- HTTP: 137 alive / 35 gold
- HTTPS: 78 alive / 10 gold
- SOCKS4: 138 alive / 62 gold
- SOCKS5: 140 alive / 45 gold

## Historical pool

- Discovered: 82962
- Ever alive: 5060
- Ever gold: 272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
