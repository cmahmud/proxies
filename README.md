# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 364
- HTTP: 91 alive / 50 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 158 alive / 148 gold
- SOCKS5: 166 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
