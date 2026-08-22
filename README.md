# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 408
- HTTP: 264 alive / 90 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 199 alive / 132 gold
- SOCKS5: 237 alive / 157 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31663
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
