# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 410
- HTTP: 90 alive / 62 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 180 alive / 166 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41469
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
