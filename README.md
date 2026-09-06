# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 389
- HTTP: 100 alive / 65 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48186
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
