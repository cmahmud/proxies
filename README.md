# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 270
- HTTP: 234 alive / 28 gold
- HTTPS: 163 alive / 3 gold
- SOCKS4: 228 alive / 134 gold
- SOCKS5: 202 alive / 105 gold

## Historical pool

- Discovered: 99078
- Ever alive: 11452
- Ever gold: 383

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
