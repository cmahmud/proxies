# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 216
- HTTP: 304 alive / 29 gold
- HTTPS: 174 alive / 7 gold
- SOCKS4: 223 alive / 119 gold
- SOCKS5: 152 alive / 61 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13518
- Ever gold: 423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
