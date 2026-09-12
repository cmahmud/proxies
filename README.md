# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 447
- HTTP: 116 alive / 86 gold
- HTTPS: 48 alive / 29 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49277
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
