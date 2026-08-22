# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 446
- HTTP: 208 alive / 107 gold
- HTTPS: 159 alive / 28 gold
- SOCKS4: 218 alive / 152 gold
- SOCKS5: 256 alive / 159 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31832
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
