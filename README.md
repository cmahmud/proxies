# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 391
- HTTP: 123 alive / 69 gold
- HTTPS: 168 alive / 25 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 176 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39846
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
