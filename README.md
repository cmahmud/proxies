# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 360
- HTTP: 228 alive / 88 gold
- HTTPS: 130 alive / 28 gold
- SOCKS4: 187 alive / 115 gold
- SOCKS5: 227 alive / 129 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
