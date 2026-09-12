# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 446
- HTTP: 119 alive / 85 gold
- HTTPS: 48 alive / 29 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49277
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
