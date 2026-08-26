# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 412
- HTTP: 90 alive / 64 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39009
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
