# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 387
- HTTP: 132 alive / 53 gold
- HTTPS: 69 alive / 15 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33609
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
