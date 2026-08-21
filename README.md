# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 366
- HTTP: 288 alive / 88 gold
- HTTPS: 196 alive / 19 gold
- SOCKS4: 203 alive / 125 gold
- SOCKS5: 226 alive / 134 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29832
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
