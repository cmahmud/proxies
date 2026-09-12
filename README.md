# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 449
- HTTP: 125 alive / 89 gold
- HTTPS: 50 alive / 31 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49295
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
