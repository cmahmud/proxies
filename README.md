# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 429
- HTTP: 97 alive / 72 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 177 alive / 168 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49050
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
