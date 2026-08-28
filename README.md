# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 401
- HTTP: 78 alive / 57 gold
- HTTPS: 36 alive / 14 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42852
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
