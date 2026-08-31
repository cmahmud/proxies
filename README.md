# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 432
- HTTP: 102 alive / 72 gold
- HTTPS: 79 alive / 27 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45473
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
