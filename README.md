# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 366
- HTTP: 92 alive / 42 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32991
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
