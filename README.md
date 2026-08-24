# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 415
- HTTP: 130 alive / 70 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33808
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
