# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 366
- HTTP: 92 alive / 50 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 158 alive / 149 gold
- SOCKS5: 165 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
