# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 395
- HTTP: 92 alive / 58 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33343
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
