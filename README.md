# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 386
- HTTP: 124 alive / 56 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33480
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
