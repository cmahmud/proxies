# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 423
- HTTP: 115 alive / 76 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44491
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
