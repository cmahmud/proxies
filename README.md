# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 440
- HTTP: 121 alive / 82 gold
- HTTPS: 77 alive / 25 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34169
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
