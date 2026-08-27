# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 438
- HTTP: 123 alive / 88 gold
- HTTPS: 130 alive / 20 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42211
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
