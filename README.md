# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 343
- HTTP: 112 alive / 46 gold
- HTTPS: 85 alive / 10 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 181 alive / 134 gold

## Historical pool

- Discovered: 171031
- Ever alive: 32805
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
