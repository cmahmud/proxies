# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 261
- HTTP: 211 alive / 30 gold
- HTTPS: 146 alive / 4 gold
- SOCKS4: 197 alive / 118 gold
- SOCKS5: 205 alive / 109 gold

## Historical pool

- Discovered: 99137
- Ever alive: 11879
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
