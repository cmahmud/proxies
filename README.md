# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 441
- HTTP: 124 alive / 89 gold
- HTTPS: 52 alive / 27 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43669
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
