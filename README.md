# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 445
- HTTP: 102 alive / 81 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 183 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49200
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
