# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 438
- HTTP: 99 alive / 78 gold
- HTTPS: 56 alive / 29 gold
- SOCKS4: 187 alive / 161 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49169
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
