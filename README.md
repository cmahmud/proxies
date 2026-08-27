# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 422
- HTTP: 117 alive / 75 gold
- HTTPS: 123 alive / 17 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41394
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
