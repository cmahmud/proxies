# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 383
- HTTP: 131 alive / 47 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33581
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
