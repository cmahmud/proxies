# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 388
- HTTP: 125 alive / 71 gold
- HTTPS: 170 alive / 19 gold
- SOCKS4: 158 alive / 146 gold
- SOCKS5: 178 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39893
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
