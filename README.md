# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 372
- HTTP: 103 alive / 47 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 182 alive / 156 gold
- SOCKS5: 209 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32991
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
