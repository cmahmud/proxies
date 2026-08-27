# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 405
- HTTP: 111 alive / 64 gold
- HTTPS: 160 alive / 13 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41128
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
