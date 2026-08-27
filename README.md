# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 405
- HTTP: 110 alive / 63 gold
- HTTPS: 124 alive / 15 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41383
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
