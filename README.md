# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 387
- HTTP: 113 alive / 53 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33585
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
