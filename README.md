# SyndProxy private pool

## Current pool

- Alive now: 638
- Gold now: 253
- HTTP: 152 alive / 35 gold
- HTTPS: 86 alive / 8 gold
- SOCKS4: 204 alive / 126 gold
- SOCKS5: 196 alive / 84 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9351
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
