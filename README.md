# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 398
- HTTP: 271 alive / 73 gold
- HTTPS: 197 alive / 26 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27465
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
