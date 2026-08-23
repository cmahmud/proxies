# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 372
- HTTP: 77 alive / 50 gold
- HTTPS: 36 alive / 14 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33044
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
