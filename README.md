# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 404
- HTTP: 96 alive / 67 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37705
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
