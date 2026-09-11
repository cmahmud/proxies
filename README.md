# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 422
- HTTP: 94 alive / 69 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 183 alive / 166 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49036
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
