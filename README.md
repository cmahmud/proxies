# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 410
- HTTP: 93 alive / 63 gold
- HTTPS: 113 alive / 18 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41445
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
