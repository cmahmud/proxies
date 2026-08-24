# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 391
- HTTP: 119 alive / 57 gold
- HTTPS: 58 alive / 13 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33528
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
