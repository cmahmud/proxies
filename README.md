# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 433
- HTTP: 90 alive / 74 gold
- HTTPS: 41 alive / 25 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49156
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
