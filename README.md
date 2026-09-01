# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 467
- HTTP: 138 alive / 93 gold
- HTTPS: 126 alive / 35 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 208 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46434
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
