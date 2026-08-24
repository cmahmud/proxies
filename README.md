# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 389
- HTTP: 127 alive / 53 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33533
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
