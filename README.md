# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 410
- HTTP: 98 alive / 70 gold
- HTTPS: 96 alive / 19 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41950
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
