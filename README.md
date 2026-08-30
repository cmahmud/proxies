# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 446
- HTTP: 110 alive / 84 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43682
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
