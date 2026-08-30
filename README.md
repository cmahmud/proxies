# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 432
- HTTP: 127 alive / 87 gold
- HTTPS: 72 alive / 32 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44079
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
