# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 340
- HTTP: 82 alive / 65 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 147 alive / 136 gold
- SOCKS5: 144 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48364
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
