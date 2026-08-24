# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 439
- HTTP: 136 alive / 81 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34539
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
