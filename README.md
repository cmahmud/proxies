# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 468
- HTTP: 164 alive / 95 gold
- HTTPS: 123 alive / 35 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45249
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
