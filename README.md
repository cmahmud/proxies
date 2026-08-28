# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 439
- HTTP: 123 alive / 85 gold
- HTTPS: 143 alive / 22 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42223
- Ever gold: 1354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
