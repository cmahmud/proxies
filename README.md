# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 427
- HTTP: 298 alive / 108 gold
- HTTPS: 173 alive / 36 gold
- SOCKS4: 223 alive / 137 gold
- SOCKS5: 233 alive / 146 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30725
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
