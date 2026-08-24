# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 390
- HTTP: 117 alive / 53 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33585
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
