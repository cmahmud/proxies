# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 387
- HTTP: 136 alive / 54 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 198 alive / 160 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33595
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
