# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 391
- HTTP: 111 alive / 63 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33163
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
