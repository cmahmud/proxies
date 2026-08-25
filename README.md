# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 410
- HTTP: 108 alive / 69 gold
- HTTPS: 85 alive / 22 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34980
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
