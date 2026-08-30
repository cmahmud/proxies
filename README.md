# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 451
- HTTP: 117 alive / 86 gold
- HTTPS: 50 alive / 32 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 180 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43678
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
