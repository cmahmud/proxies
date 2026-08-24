# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 415
- HTTP: 131 alive / 71 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33806
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
