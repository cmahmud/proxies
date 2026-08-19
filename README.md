# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 493
- HTTP: 279 alive / 120 gold
- HTTPS: 186 alive / 70 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 229 alive / 155 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16792
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
