# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 422
- HTTP: 100 alive / 64 gold
- HTTPS: 76 alive / 22 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36047
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
