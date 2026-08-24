# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 399
- HTTP: 125 alive / 66 gold
- HTTPS: 61 alive / 10 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33311
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
