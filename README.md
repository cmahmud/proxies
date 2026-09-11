# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 422
- HTTP: 95 alive / 68 gold
- HTTPS: 46 alive / 21 gold
- SOCKS4: 191 alive / 162 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48920
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
