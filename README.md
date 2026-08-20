# SyndProxy private pool

## Current pool

- Alive now: 1695
- Gold now: 656
- HTTP: 610 alive / 214 gold
- HTTPS: 493 alive / 115 gold
- SOCKS4: 242 alive / 160 gold
- SOCKS5: 350 alive / 167 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24154
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
