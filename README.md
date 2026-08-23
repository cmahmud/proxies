# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 202
- HTTP: 226 alive / 44 gold
- HTTPS: 56 alive / 6 gold
- SOCKS4: 96 alive / 67 gold
- SOCKS5: 146 alive / 85 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32735
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
