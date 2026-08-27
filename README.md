# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 407
- HTTP: 113 alive / 64 gold
- HTTPS: 162 alive / 13 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41135
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
