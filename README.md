# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 426
- HTTP: 98 alive / 72 gold
- HTTPS: 53 alive / 25 gold
- SOCKS4: 196 alive / 168 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49081
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
