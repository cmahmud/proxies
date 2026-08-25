# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 418
- HTTP: 101 alive / 61 gold
- HTTPS: 82 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35796
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
