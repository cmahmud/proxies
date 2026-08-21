# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 364
- HTTP: 217 alive / 75 gold
- HTTPS: 187 alive / 22 gold
- SOCKS4: 194 alive / 132 gold
- SOCKS5: 239 alive / 135 gold

## Historical pool

- Discovered: 156893
- Ever alive: 29646
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
