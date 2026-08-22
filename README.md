# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 410
- HTTP: 320 alive / 81 gold
- HTTPS: 256 alive / 25 gold
- SOCKS4: 223 alive / 151 gold
- SOCKS5: 251 alive / 153 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32291
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
