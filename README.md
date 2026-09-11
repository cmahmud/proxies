# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 434
- HTTP: 106 alive / 76 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49134
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
