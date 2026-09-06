# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 382
- HTTP: 105 alive / 68 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 165 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
