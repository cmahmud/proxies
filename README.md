# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 382
- HTTP: 94 alive / 45 gold
- HTTPS: 58 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33577
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
