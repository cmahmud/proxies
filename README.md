# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 433
- HTTP: 122 alive / 88 gold
- HTTPS: 121 alive / 18 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 199 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42215
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
