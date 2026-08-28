# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 401
- HTTP: 76 alive / 55 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42790
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
