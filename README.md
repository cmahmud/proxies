# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 396
- HTTP: 247 alive / 92 gold
- HTTPS: 177 alive / 28 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 206 alive / 136 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31609
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
