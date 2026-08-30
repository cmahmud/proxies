# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 480
- HTTP: 159 alive / 102 gold
- HTTPS: 124 alive / 41 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44972
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
