# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 404
- HTTP: 89 alive / 65 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 174 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37672
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
