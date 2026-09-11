# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 434
- HTTP: 105 alive / 77 gold
- HTTPS: 56 alive / 26 gold
- SOCKS4: 187 alive / 169 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49094
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
