# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 407
- HTTP: 102 alive / 62 gold
- HTTPS: 166 alive / 16 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41015
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
