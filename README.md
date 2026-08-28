# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 436
- HTTP: 121 alive / 87 gold
- HTTPS: 129 alive / 20 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42216
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
