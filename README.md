# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 540
- HTTP: 418 alive / 154 gold
- HTTPS: 293 alive / 107 gold
- SOCKS4: 206 alive / 132 gold
- SOCKS5: 205 alive / 147 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
