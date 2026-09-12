# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 325
- HTTP: 79 alive / 64 gold
- HTTPS: 45 alive / 24 gold
- SOCKS4: 126 alive / 106 gold
- SOCKS5: 151 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49497
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
