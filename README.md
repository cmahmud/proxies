# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 420
- HTTP: 91 alive / 64 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36077
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
