# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 381
- HTTP: 112 alive / 46 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
