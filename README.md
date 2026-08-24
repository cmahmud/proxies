# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 439
- HTTP: 114 alive / 81 gold
- HTTPS: 75 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34212
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
