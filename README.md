# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 410
- HTTP: 98 alive / 59 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41482
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
