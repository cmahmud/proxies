# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 424
- HTTP: 123 alive / 65 gold
- HTTPS: 79 alive / 21 gold
- SOCKS4: 197 alive / 161 gold
- SOCKS5: 228 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35879
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
