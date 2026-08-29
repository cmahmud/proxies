# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 421
- HTTP: 114 alive / 77 gold
- HTTPS: 57 alive / 29 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
