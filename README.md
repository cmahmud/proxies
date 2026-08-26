# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 407
- HTTP: 96 alive / 61 gold
- HTTPS: 74 alive / 17 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39107
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
