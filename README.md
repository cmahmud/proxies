# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 403
- HTTP: 92 alive / 62 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41439
- Ever gold: 1329

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
