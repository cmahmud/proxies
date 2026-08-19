# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 542
- HTTP: 351 alive / 171 gold
- HTTPS: 231 alive / 92 gold
- SOCKS4: 206 alive / 137 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 122387
- Ever alive: 18653
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
