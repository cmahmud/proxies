# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 420
- HTTP: 113 alive / 75 gold
- HTTPS: 128 alive / 17 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41389
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
