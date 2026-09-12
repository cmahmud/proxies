# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 426
- HTTP: 98 alive / 75 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49483
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
