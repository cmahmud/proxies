# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 412
- HTTP: 106 alive / 71 gold
- HTTPS: 124 alive / 23 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41887
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
