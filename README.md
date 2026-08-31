# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 460
- HTTP: 158 alive / 89 gold
- HTTPS: 123 alive / 35 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 240 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45322
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
