# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 445
- HTTP: 124 alive / 88 gold
- HTTPS: 49 alive / 26 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49268
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
