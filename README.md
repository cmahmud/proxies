# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 401
- HTTP: 85 alive / 55 gold
- HTTPS: 59 alive / 20 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41693
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
