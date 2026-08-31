# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 438
- HTTP: 115 alive / 77 gold
- HTTPS: 62 alive / 27 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 200 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45549
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
