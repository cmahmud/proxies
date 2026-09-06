# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 403
- HTTP: 105 alive / 77 gold
- HTTPS: 42 alive / 16 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48190
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
