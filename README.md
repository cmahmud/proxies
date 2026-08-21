# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 396
- HTTP: 274 alive / 83 gold
- HTTPS: 143 alive / 19 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 231 alive / 147 gold

## Historical pool

- Discovered: 155802
- Ever alive: 29400
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
