# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 416
- HTTP: 102 alive / 69 gold
- HTTPS: 110 alive / 24 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41816
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
