# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 520
- HTTP: 404 alive / 158 gold
- HTTPS: 287 alive / 88 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 195 alive / 133 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18489
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
