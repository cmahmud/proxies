# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 395
- HTTP: 118 alive / 60 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33527
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
