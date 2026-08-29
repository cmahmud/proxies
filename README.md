# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 438
- HTTP: 122 alive / 88 gold
- HTTPS: 52 alive / 26 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43669
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
