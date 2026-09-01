# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 427
- HTTP: 87 alive / 69 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47296
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
