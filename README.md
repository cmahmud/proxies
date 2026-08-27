# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 417
- HTTP: 121 alive / 72 gold
- HTTPS: 122 alive / 16 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41386
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
