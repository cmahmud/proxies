# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 523
- HTTP: 326 alive / 158 gold
- HTTPS: 238 alive / 87 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 196 alive / 137 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18457
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
