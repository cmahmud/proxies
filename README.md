# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 384
- HTTP: 263 alive / 87 gold
- HTTPS: 186 alive / 26 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 210 alive / 132 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31599
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
