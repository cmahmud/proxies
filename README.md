# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 424
- HTTP: 101 alive / 64 gold
- HTTPS: 73 alive / 24 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35958
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
