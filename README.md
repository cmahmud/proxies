# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 406
- HTTP: 84 alive / 57 gold
- HTTPS: 80 alive / 22 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42722
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
