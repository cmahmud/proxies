# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 434
- HTTP: 118 alive / 76 gold
- HTTPS: 67 alive / 29 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45535
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
