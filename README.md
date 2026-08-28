# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 404
- HTTP: 82 alive / 61 gold
- HTTPS: 84 alive / 17 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42915
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
