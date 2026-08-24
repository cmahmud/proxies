# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 383
- HTTP: 100 alive / 48 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33571
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
