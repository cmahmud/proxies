# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 427
- HTTP: 136 alive / 79 gold
- HTTPS: 64 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33941
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
