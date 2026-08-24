# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 395
- HTTP: 112 alive / 56 gold
- HTTPS: 58 alive / 15 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33530
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
