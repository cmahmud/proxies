# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 445
- HTTP: 128 alive / 88 gold
- HTTPS: 75 alive / 35 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 202 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44273
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
