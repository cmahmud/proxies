# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 408
- HTTP: 365 alive / 89 gold
- HTTPS: 242 alive / 30 gold
- SOCKS4: 221 alive / 133 gold
- SOCKS5: 238 alive / 156 gold

## Historical pool

- Discovered: 163042
- Ever alive: 31685
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
