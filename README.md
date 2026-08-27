# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 405
- HTTP: 125 alive / 62 gold
- HTTPS: 157 alive / 12 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40855
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
