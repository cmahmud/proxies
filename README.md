# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 435
- HTTP: 116 alive / 79 gold
- HTTPS: 56 alive / 29 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44304
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
