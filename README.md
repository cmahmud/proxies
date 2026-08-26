# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 407
- HTTP: 105 alive / 63 gold
- HTTPS: 93 alive / 14 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39295
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
