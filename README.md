# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 398
- HTTP: 180 alive / 76 gold
- HTTPS: 130 alive / 19 gold
- SOCKS4: 220 alive / 151 gold
- SOCKS5: 223 alive / 152 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27351
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
