# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 391
- HTTP: 126 alive / 69 gold
- HTTPS: 175 alive / 25 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 176 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39843
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
