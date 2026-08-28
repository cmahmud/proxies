# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 441
- HTTP: 119 alive / 90 gold
- HTTPS: 141 alive / 22 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 197 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42219
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
