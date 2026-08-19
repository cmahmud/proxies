# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 554
- HTTP: 334 alive / 171 gold
- HTTPS: 224 alive / 91 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 215 alive / 147 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19160
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
