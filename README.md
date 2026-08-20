# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 372
- HTTP: 184 alive / 65 gold
- HTTPS: 154 alive / 18 gold
- SOCKS4: 211 alive / 152 gold
- SOCKS5: 199 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25924
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
