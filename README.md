# SyndProxy validated proxy pool

## Current pool

- Alive now: 459
- Gold now: 193
- HTTP: 158 alive / 40 gold
- HTTPS: 45 alive / 8 gold
- SOCKS4: 130 alive / 64 gold
- SOCKS5: 126 alive / 81 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32720
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
