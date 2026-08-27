# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 398
- HTTP: 100 alive / 62 gold
- HTTPS: 105 alive / 16 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41428
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
