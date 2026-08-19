# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 319
- HTTP: 273 alive / 49 gold
- HTTPS: 187 alive / 10 gold
- SOCKS4: 205 alive / 132 gold
- SOCKS5: 194 alive / 128 gold

## Historical pool

- Discovered: 128086
- Ever alive: 20031
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
