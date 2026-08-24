# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 388
- HTTP: 109 alive / 51 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33615
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
