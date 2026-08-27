# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 416
- HTTP: 108 alive / 70 gold
- HTTPS: 140 alive / 17 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41289
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
