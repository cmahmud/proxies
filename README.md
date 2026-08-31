# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 423
- HTTP: 86 alive / 59 gold
- HTTPS: 66 alive / 32 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45497
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
