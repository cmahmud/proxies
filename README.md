# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 385
- HTTP: 167 alive / 69 gold
- HTTPS: 138 alive / 19 gold
- SOCKS4: 193 alive / 142 gold
- SOCKS5: 230 alive / 155 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25560
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
