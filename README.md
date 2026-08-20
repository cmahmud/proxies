# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 396
- HTTP: 181 alive / 73 gold
- HTTPS: 117 alive / 19 gold
- SOCKS4: 199 alive / 149 gold
- SOCKS5: 211 alive / 155 gold

## Historical pool

- Discovered: 147183
- Ever alive: 25814
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
