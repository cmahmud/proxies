# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 376
- HTTP: 97 alive / 58 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 174129
- Ever alive: 33060
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
