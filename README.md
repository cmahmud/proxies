# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 400
- HTTP: 90 alive / 62 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37581
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
