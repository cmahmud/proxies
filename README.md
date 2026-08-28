# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 396
- HTTP: 77 alive / 56 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 175 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42814
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
