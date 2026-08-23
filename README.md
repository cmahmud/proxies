# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 351
- HTTP: 130 alive / 38 gold
- HTTPS: 97 alive / 8 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 202 alive / 153 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32916
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
