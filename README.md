# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 397
- HTTP: 90 alive / 70 gold
- HTTPS: 33 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48243
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
