# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 361
- HTTP: 90 alive / 75 gold
- HTTPS: 61 alive / 32 gold
- SOCKS4: 166 alive / 76 gold
- SOCKS5: 209 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1556

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
