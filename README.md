# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 400
- HTTP: 80 alive / 57 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42848
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
