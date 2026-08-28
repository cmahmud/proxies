# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 422
- HTTP: 96 alive / 76 gold
- HTTPS: 110 alive / 21 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42512
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
