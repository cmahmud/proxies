# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 382
- HTTP: 126 alive / 45 gold
- HTTPS: 50 alive / 12 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33581
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
