# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 346
- HTTP: 161 alive / 72 gold
- HTTPS: 110 alive / 18 gold
- SOCKS4: 175 alive / 121 gold
- SOCKS5: 195 alive / 135 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25574
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
