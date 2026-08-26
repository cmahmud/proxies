# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 399
- HTTP: 101 alive / 65 gold
- HTTPS: 72 alive / 16 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38704
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
