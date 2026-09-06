# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 411
- HTTP: 110 alive / 79 gold
- HTTPS: 58 alive / 20 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
