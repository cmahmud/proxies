# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 411
- HTTP: 106 alive / 71 gold
- HTTPS: 129 alive / 23 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41881
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
