# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 386
- HTTP: 120 alive / 53 gold
- HTTPS: 66 alive / 15 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33587
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
