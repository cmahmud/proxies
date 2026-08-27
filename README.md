# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 422
- HTTP: 111 alive / 70 gold
- HTTPS: 134 alive / 19 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41278
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
