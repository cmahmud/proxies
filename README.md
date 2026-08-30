# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 430
- HTTP: 122 alive / 87 gold
- HTTPS: 78 alive / 32 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 172 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44079
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
