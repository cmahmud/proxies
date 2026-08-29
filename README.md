# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 402
- HTTP: 98 alive / 71 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43296
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
