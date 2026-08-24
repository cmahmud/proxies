# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 383
- HTTP: 95 alive / 43 gold
- HTTPS: 49 alive / 13 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
