# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 385
- HTTP: 214 alive / 89 gold
- HTTPS: 163 alive / 28 gold
- SOCKS4: 210 alive / 138 gold
- SOCKS5: 212 alive / 130 gold

## Historical pool

- Discovered: 162766
- Ever alive: 31630
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
