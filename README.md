# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 386
- HTTP: 98 alive / 65 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48187
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
