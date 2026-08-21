# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 419
- HTTP: 352 alive / 110 gold
- HTTPS: 199 alive / 28 gold
- SOCKS4: 201 alive / 132 gold
- SOCKS5: 234 alive / 149 gold

## Historical pool

- Discovered: 160198
- Ever alive: 30628
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
