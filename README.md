# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 381
- HTTP: 94 alive / 45 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33565
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
