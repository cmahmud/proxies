# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 404
- HTTP: 104 alive / 62 gold
- HTTPS: 78 alive / 17 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39073
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
