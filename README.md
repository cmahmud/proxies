# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 439
- HTTP: 115 alive / 89 gold
- HTTPS: 135 alive / 21 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42218
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
