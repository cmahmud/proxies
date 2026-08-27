# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 417
- HTTP: 105 alive / 64 gold
- HTTPS: 142 alive / 23 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41300
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
