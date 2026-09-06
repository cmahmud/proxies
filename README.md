# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 394
- HTTP: 107 alive / 77 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48193
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
