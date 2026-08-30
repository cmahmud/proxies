# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 425
- HTTP: 105 alive / 73 gold
- HTTPS: 65 alive / 28 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44355
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
