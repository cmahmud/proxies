# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 404
- HTTP: 111 alive / 68 gold
- HTTPS: 79 alive / 20 gold
- SOCKS4: 161 alive / 158 gold
- SOCKS5: 170 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37174
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
