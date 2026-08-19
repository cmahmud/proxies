# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 481
- HTTP: 341 alive / 146 gold
- HTTPS: 250 alive / 87 gold
- SOCKS4: 211 alive / 118 gold
- SOCKS5: 226 alive / 130 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17573
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
