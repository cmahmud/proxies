# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 401
- HTTP: 118 alive / 75 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33275
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
