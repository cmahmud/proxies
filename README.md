# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 464
- HTTP: 121 alive / 91 gold
- HTTPS: 121 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 215 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45968
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
