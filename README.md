# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 387
- HTTP: 104 alive / 72 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 166 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
