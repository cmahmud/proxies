# SyndProxy validated proxy pool

## Current pool

- Alive now: 443
- Gold now: 368
- HTTP: 81 alive / 47 gold
- HTTPS: 25 alive / 11 gold
- SOCKS4: 165 alive / 153 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 173752
- Ever alive: 33024
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
