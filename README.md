# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 385
- HTTP: 77 alive / 48 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41628
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
