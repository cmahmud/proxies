# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 497
- HTTP: 277 alive / 122 gold
- HTTPS: 193 alive / 70 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 228 alive / 155 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16784
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
