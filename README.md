# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 368
- HTTP: 149 alive / 80 gold
- HTTPS: 63 alive / 24 gold
- SOCKS4: 144 alive / 116 gold
- SOCKS5: 174 alive / 148 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47992
- Ever gold: 1507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
