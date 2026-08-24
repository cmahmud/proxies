# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 389
- HTTP: 120 alive / 51 gold
- HTTPS: 69 alive / 15 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33609
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
