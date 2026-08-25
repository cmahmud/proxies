# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 400
- HTTP: 95 alive / 69 gold
- HTTPS: 79 alive / 18 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 165 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37457
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
