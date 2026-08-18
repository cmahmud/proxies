# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 353
- HTTP: 321 alive / 53 gold
- HTTPS: 190 alive / 14 gold
- SOCKS4: 254 alive / 147 gold
- SOCKS5: 231 alive / 139 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15103
- Ever gold: 480

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
