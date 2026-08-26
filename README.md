# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 404
- HTTP: 104 alive / 68 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38947
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
