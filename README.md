# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 392
- HTTP: 122 alive / 56 gold
- HTTPS: 73 alive / 14 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33523
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
