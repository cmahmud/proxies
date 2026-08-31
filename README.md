# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 481
- HTTP: 144 alive / 99 gold
- HTTPS: 120 alive / 43 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45104
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
