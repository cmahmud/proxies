# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 492
- HTTP: 281 alive / 120 gold
- HTTPS: 190 alive / 70 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 228 alive / 154 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16792
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
