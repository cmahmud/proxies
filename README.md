# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 398
- HTTP: 84 alive / 57 gold
- HTTPS: 90 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 168 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42964
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
