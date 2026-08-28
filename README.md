# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 404
- HTTP: 86 alive / 58 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42740
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
