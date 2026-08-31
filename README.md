# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 436
- HTTP: 112 alive / 75 gold
- HTTPS: 62 alive / 29 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45553
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
