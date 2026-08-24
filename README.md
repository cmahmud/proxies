# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 381
- HTTP: 96 alive / 42 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
