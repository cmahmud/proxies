# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 387
- HTTP: 115 alive / 50 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33612
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
