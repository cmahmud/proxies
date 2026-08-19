# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 517
- HTTP: 435 alive / 154 gold
- HTTPS: 291 alive / 85 gold
- SOCKS4: 196 alive / 143 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18507
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
