# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 337
- HTTP: 262 alive / 60 gold
- HTTPS: 179 alive / 12 gold
- SOCKS4: 195 alive / 143 gold
- SOCKS5: 181 alive / 122 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20171
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
