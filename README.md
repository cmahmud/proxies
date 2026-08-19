# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 496
- HTTP: 393 alive / 122 gold
- HTTPS: 265 alive / 74 gold
- SOCKS4: 230 alive / 149 gold
- SOCKS5: 276 alive / 151 gold

## Historical pool

- Discovered: 114412
- Ever alive: 17027
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
