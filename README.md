# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 463
- HTTP: 119 alive / 91 gold
- HTTPS: 51 alive / 30 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 195 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49419
- Ever gold: 1582

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
