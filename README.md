# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 379
- HTTP: 91 alive / 44 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33565
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
