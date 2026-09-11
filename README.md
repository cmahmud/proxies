# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 413
- HTTP: 88 alive / 65 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 176 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48852
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
