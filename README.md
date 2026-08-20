# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 355
- HTTP: 170 alive / 71 gold
- HTTPS: 151 alive / 24 gold
- SOCKS4: 183 alive / 130 gold
- SOCKS5: 190 alive / 130 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26642
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
