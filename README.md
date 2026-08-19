# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 492
- HTTP: 300 alive / 119 gold
- HTTPS: 196 alive / 70 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 236 alive / 155 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16812
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
