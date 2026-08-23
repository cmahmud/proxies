# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 336
- HTTP: 107 alive / 40 gold
- HTTPS: 67 alive / 6 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 185 alive / 138 gold

## Historical pool

- Discovered: 171578
- Ever alive: 32894
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
