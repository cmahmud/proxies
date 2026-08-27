# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 387
- HTTP: 74 alive / 51 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41630
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
