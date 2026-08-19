# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 317
- HTTP: 232 alive / 61 gold
- HTTPS: 161 alive / 8 gold
- SOCKS4: 208 alive / 118 gold
- SOCKS5: 194 alive / 130 gold

## Historical pool

- Discovered: 129264
- Ever alive: 20144
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
