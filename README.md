# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 391
- HTTP: 120 alive / 53 gold
- HTTPS: 62 alive / 13 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33583
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
