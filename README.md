# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 385
- HTTP: 110 alive / 62 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 186 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39332
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
