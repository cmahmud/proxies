# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 202
- HTTP: 230 alive / 41 gold
- HTTPS: 83 alive / 6 gold
- SOCKS4: 95 alive / 67 gold
- SOCKS5: 149 alive / 88 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32747
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
