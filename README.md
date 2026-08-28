# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 436
- HTTP: 124 alive / 88 gold
- HTTPS: 123 alive / 19 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42215
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
