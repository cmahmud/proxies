# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 373
- HTTP: 296 alive / 96 gold
- HTTPS: 198 alive / 24 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 202 alive / 113 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28983
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
