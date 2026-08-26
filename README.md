# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 400
- HTTP: 93 alive / 62 gold
- HTTPS: 79 alive / 14 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39213
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
