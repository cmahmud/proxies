# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 380
- HTTP: 115 alive / 43 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33579
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
