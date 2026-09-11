# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 372
- HTTP: 181 alive / 89 gold
- HTTPS: 41 alive / 30 gold
- SOCKS4: 96 alive / 75 gold
- SOCKS5: 212 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48643
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
