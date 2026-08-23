# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 339
- HTTP: 127 alive / 38 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 192 alive / 142 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32884
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
