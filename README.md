# SyndProxy private pool

## Current pool

- Alive now: 492
- Gold now: 213
- HTTP: 136 alive / 35 gold
- HTTPS: 79 alive / 12 gold
- SOCKS4: 137 alive / 96 gold
- SOCKS5: 140 alive / 70 gold

## Historical pool

- Discovered: 82962
- Ever alive: 5060
- Ever gold: 284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
