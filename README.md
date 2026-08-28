# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 401
- HTTP: 82 alive / 58 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42849
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
