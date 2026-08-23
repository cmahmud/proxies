# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 351
- HTTP: 117 alive / 37 gold
- HTTPS: 79 alive / 8 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 203 alive / 153 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32918
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
